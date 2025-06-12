/**
 * This is a file level JSDoc comment
 * Total JSDoc comments: 3
 * Total classes: 1
 * Total functions: 4
 * Total variables: 7
 * Total comments: 5
 * Total keywords used: 15 (const, let, var, function, class, if, else, return, async, await, try, catch, import, export, default)
 * Total identifiers: 10
 * Total literals: 8
 */

// Constants and variables
const MAX_VALUE = 1000;
let message = 'JavaScript Test Sample';
const numbers = [1, 2, 3, 4, 5];

/**
 * Class representing a data processor
 * @class DataProcessor
 */
class DataProcessor {
    constructor(multiplier) {
        this.multiplier = multiplier;
        this.processed = 0;
    }

    /**
     * Process a single number
     * @param {number} input - The number to process
     * @returns {number} The processed result
     */
    processNumber(input) {
        this.processed++;
        return input * this.multiplier;
    }

    // Array processing method
    processArray(arr) {
        return arr.map(num => this.processNumber(num));
    }

    // Async operation demonstration
    async fetchAndProcess(url) {
        try {
            const response = await fetch(url);
            const data = await response.json();
            return this.processArray(data);
        } catch (error) {
            console.error('Error:', error);
            return [];
        }
    }
}

// Function outside class
function calculateSum(arr) {
    return arr.reduce((sum, current) => sum + current, 0);
}

// Main execution
const processor = new DataProcessor(2.5);
const processedNumbers = processor.processArray(numbers);
const sum = calculateSum(processedNumbers);

console.log('Original numbers:', numbers);
console.log('Processed numbers:', processedNumbers);
console.log('Sum:', sum);

// Export for module usage
export default DataProcessor; 