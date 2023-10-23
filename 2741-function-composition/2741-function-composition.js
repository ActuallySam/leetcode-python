/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {

	return function(x) {
        if (functions.length == 0)
            return x
        
        var updated_value = x;
        for (let i=functions.length - 1; i>=0; i--) {
            updated_value = functions[i](updated_value);
        }

        return updated_value
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */