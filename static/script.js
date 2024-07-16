document.addEventListener('DOMContentLoaded', () => {
    const output = document.getElementById('output');
    const userInput = document.getElementById('user-input');
    const startBtn = document.getElementById('start-btn');

    const questions = [
        {
            question: 'What are you here for today?',
            options: ['Get latest fashion updates', 'Get personalized recommendation']
        },
        {
            question: 'What is the occasion you are shopping for?',
            options: ['Western', 'Traditional']
        },
        {
            question: 'What is your size?',
            options: ['Small', 'Medium', 'Large']
        },
        {
            question: 'What is your body type?',
            options: ['Pear shape', 'Apple shape', 'Hourglass shape', 'Rectangle shape']
        },
        {
            question: 'What is your color preference?',
            options: ['Light colors', 'Dark colors']
        },
        {
            question: 'What is your price range?',
            options: ['Below 2300', 'Below 900', 'Below 1500', 'Below 5000']
        }
    ];

    let currentQuestionIndex = 0;
    const userResponses = [];

    startBtn.addEventListener('click', () => {
        startBtn.remove();
        askQuestion();
    });

    function askQuestion() {
        const question = questions[currentQuestionIndex];
        addMessage('bot', question.question);

        userInput.innerHTML = '<div class="option-buttons"></div>';
        const optionButtons = userInput.querySelector('.option-buttons');

        question.options.forEach(option => {
            const button = document.createElement('button');
            button.textContent = option;
            button.addEventListener('click', () => handleResponse(option));
            optionButtons.appendChild(button);
        });
    }

    function handleResponse(response) {
        addMessage('user', response);
        userResponses.push(response);

        if (response === 'Get latest fashion updates') {
            fetchNews();
        } else if (response === 'Get personalized recommendation' || currentQuestionIndex > 0) {
            if (currentQuestionIndex < questions.length - 1) {
                currentQuestionIndex++;
                askQuestion();
            } else {
                getRecommendations();
            }
        }
    }

    function fetchNews() {
        const apiKey = 'dff7360ee33b454fbcc07a5a4c4cddd0';  // Replace with your News API key
        const url = `https://newsapi.org/v2/everything?q=fashion%20tips%20OR%20latest%20fashion%20trends&language=en&sources=the-times-of-india,ndtv,hindustan-times,the-hindu,the-indian-express,business-standard,the-economic-times&apiKey=${apiKey}`;
        
        fetch(url)
            .then(response => response.json())
            .then(data => {
                if (data.status === 'ok') {
                    addMessage('bot', 'Top 10 Latest Fashion Articles:');
                    const articles = data.articles.slice(0, 10);
                    articles.forEach(article => {
                        addMessage('bot', `<a href="${article.url}" target="_blank">${article.title} - ${article.source.name}</a>`);
                    });
                } else if (data.code === 'rateLimited') {
                    addMessage('bot', 'Rate limit exceeded. Please try again later.');
                } else {
                    addMessage('bot', 'Sorry, something went wrong while fetching the news.');
                }
            })
            .catch(error => {
                console.error('Error fetching news:', error);
                addMessage('bot', 'Sorry, something went wrong while fetching the news.');
            });

        userInput.innerHTML = '<button id="restart-btn">Restart</button>';
        document.getElementById('restart-btn').addEventListener('click', () => {
            window.location.reload();
        });
    }

    function getRecommendations() {
        addMessage('bot', 'Fetching recommendations based on your preferences...');
        
        fetch('/get-recommendations', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ responses: userResponses })
        })
        .then(response => response.json())
        .then(data => {
            console.log('Backend response:', data);
            displayRecommendations(data.products);
        })
        .catch(error => {
            console.error('Error fetching recommendations:', error);
            addMessage('bot', 'Sorry, something went wrong while fetching recommendations.');
        });
    }

    function displayRecommendations(products) {
        output.innerHTML = '';
    
        if (Array.isArray(products) && products.length > 0) {
            products.forEach(product => {
                const productDiv = document.createElement('div');
                productDiv.classList.add('product');
    
                // Create image element
                const img = document.createElement('img');
                img.src = product.Imagelink || 'default-image.jpg'; // Use a default image if none is provided
                img.alt = 'Product Image'; // Default alt text
                productDiv.appendChild(img);
    
                // Create link element
                const link = document.createElement('a');
                link.href = product.Link || '#'; // Ensure the link is valid
                link.target = '_blank';
                link.textContent = 'View Product'; // Default text for the link
                productDiv.appendChild(link);
    
                output.appendChild(productDiv);
            });
        } else {
            addMessage('bot', 'No recommendations found.');
        }
    }
    
    

    function addMessage(sender, text) {
        const message = document.createElement('div');
        message.classList.add('message', sender);

        const bubble = document.createElement('div');
        bubble.classList.add('bubble');
        bubble.innerHTML = text;

        message.appendChild(bubble);
        output.appendChild(message);
        output.scrollTop = output.scrollHeight;
    }

    // Function to share chat content on WhatsApp
    function shareOnWhatsApp() {
        const output = document.getElementById('output');
        const chatContent = Array.from(output.querySelectorAll('.message')).map(msg => msg.textContent).join('\n');
        const encodedChatContent = encodeURIComponent(chatContent);
        const whatsappURL = `https://api.whatsapp.com/send?text=${encodedChatContent}`;
    
        const whatsappLink = document.createElement('a');
        whatsappLink.href = whatsappURL;
        whatsappLink.textContent = 'Click here to share the chat content';
        whatsappLink.target = '_blank';
    
        const shareToFriendsParagraph = document.getElementById('shareToFriends');
        shareToFriendsParagraph.textContent = ''; // Clear existing text
        shareToFriendsParagraph.appendChild(whatsappLink);
    }
    
    // Attach event listener
    document.getElementById('shareToFriends').addEventListener('click', shareOnWhatsApp);
    
    
    
});
