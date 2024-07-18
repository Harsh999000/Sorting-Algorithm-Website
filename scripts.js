let selectedAlgorithm = null;

const algorithmNames = {
    selectionSort: "Selection Sort",
    bubbleSort: "Bubble Sort",
    insertionSort: "Insertion Sort",
    mergeSort: "Merge Sort",
    quickSort: "Quick Sort",
    heapSort: "Heap Sort"
};

function selectAlgorithm(algorithm) {
    selectedAlgorithm = algorithm;
    
    // Remove 'active' class from all buttons
    document.querySelectorAll('.sidebar button').forEach(button => {
        button.classList.remove('active');
    });
    
    // Add 'active' class to the selected button
    const button = document.querySelector(`.sidebar button[onclick*='${algorithm}']`);
    if (button) {
        button.classList.add('active');
    }
    
    // Update the header with the selected algorithm name
    const codeHeader = document.getElementById('codeHeader');
    if (algorithm in algorithmNames) {
        codeHeader.textContent = `Python Code for ${algorithmNames[algorithm]}`;
    } else {
        codeHeader.textContent = 'Python Code for the Selected Algorithm';
    }
}


function handleSubmit() {
    const numElements = document.getElementById('numElements').value;
    const elementInputs = document.getElementById('elementInputs');
    const arrayInputs = document.getElementById('arrayInputs');
    const submitButton = document.getElementById('submitButton');
    const runButton = document.getElementById('runButton');
    
    if (numElements < 1 || numElements > 10) {
        alert("Please enter details as per instructions");
        return;
    }
    
    arrayInputs.innerHTML = '';
    
    for (let i = 0; i < numElements; i++) {
        const input = document.createElement('input');
        input.type = 'number';
        input.min = -999;
        input.max = 999;
        arrayInputs.appendChild(input);
    }
    
    elementInputs.style.display = 'block';
    runButton.style.display = 'block';
    submitButton.textContent = 'Reset';
    submitButton.onclick = () => {
        // Clear all fields and reset states
        document.getElementById('numElements').value = '';
        elementInputs.style.display = 'none';
        arrayInputs.innerHTML = '';
        runButton.style.display = 'none';
        submitButton.textContent = 'Submit';
        submitButton.onclick = handleSubmit;
        document.querySelectorAll('.sidebar button').forEach(button => {
            button.classList.remove('active');
        });
        document.getElementById('demo').innerHTML = '';
        document.getElementById('code').innerHTML = '';
        selectedAlgorithm = null;
        document.getElementById('codeHeader').textContent = 'Python Code for the Selected Algorithm';
    };
}

function runAlgorithm() {
    if (!selectedAlgorithm) {
        alert("Please select an algorithm to visualize");
        return;
    }

    const numElements = document.getElementById('numElements').value;
    const arrayInputs = Array.from(document.querySelectorAll('#arrayInputs input')).map(input => input.value);

    if (arrayInputs.length === parseInt(numElements) && arrayInputs.every(num => num >= -999 && num <= 999)) {
        fetch(`/run_algorithm?algorithm=${selectedAlgorithm}&array=${arrayInputs.join(',')}`)
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    alert(data.error);
                } else {
                    // Format visualization with step numbers
                    const steps = data.visualization.split('\n').filter(step => step.trim() !== '').map((step, index) => `Step ${index + 1}: ${step.trim()}`).join('\n');
                    document.getElementById('demo').innerHTML = `<pre>${steps}</pre>`; // Wrap in <pre> for proper formatting
                    document.getElementById('code').innerHTML = `<h2 id="codeHeader">Python Code for ${algorithmNames[selectedAlgorithm]}</h2><pre>${data.code}</pre>`;
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred while fetching the data.');
            });
    } else {
        alert("Please enter details as per instructions");
    }
}
