class Solution {
public:
    int smallestRepunitDivByK(int k) {

        // Remainder after forming repunit numbers step-by-step
        int rem = 0;

        // Try repunits of increasing length: 1, 11, 111, ...
        // Bound = 2*k ensures we detect cycles and avoid infinite loops
        for (int length = 1; length <= k * 2; length++) 
        {
            // Add a new digit '1': (previous_number * 10 + 1) % k
            rem = (rem * 10 + 1) % k;

            // If remainder becomes 0, this repunit is divisible by k
            if (rem == 0) 
                return length;
        }

        // If no repunit divides k
        return -1;
    }
};