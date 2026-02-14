document.addEventListener("DOMContentLoaded", function() {

    
    // LOADING SCREEN & VALIDATION LOGIC
    

    function handleFormSubmit(event) {
        const form = event.target;
        
        // 1. Sanity Check: Rainfall 
        // If user enters 20000 instead of 200 mm
        const rainInputs = form.querySelectorAll('input[name*="rain"]');
        for (let input of rainInputs) {
            if (parseFloat(input.value) > 3000) {
                alert(" Warning: Rainfall value is too high! Please enter value in mm (e.g., 200).");
                event.preventDefault(); // Stop the form
                return;
            }
        }

        //  2. Sanity Check: pH Level 
        // pH must be between 0 and 14
        const phInputs = form.querySelectorAll('input[name*="ph"]');
        for (let input of phInputs) {
            let val = parseFloat(input.value);
            if (val < 0 || val > 14) {
                alert(" Error: pH level must be between 0 and 14.");
                event.preventDefault(); // Stop the form
                return;
            }
        }

        // 3. Show Loading Overlay
        // Only shows if checks pass
        document.getElementById('loading-overlay').style.display = 'flex';
    }

    // Attach this logic to both forms
    const cropForm = document.getElementById('cropForm');
    if (cropForm) cropForm.addEventListener('submit', handleFormSubmit);

    const fertForm = document.getElementById('fertForm');
    if (fertForm) fertForm.addEventListener('submit', handleFormSubmit);

});