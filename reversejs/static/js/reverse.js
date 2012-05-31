var reversejs = (function () {
    var patterns = {};
    var exports = {};

    var interpolate = function(s, args) {
        var i = 0;
        return s.replace(/%(?:\(([^)]+)\))?([%diouxXeEfFgGcrs])/g, function (match, v, t) {
            if (t == "%") return "%";
            return args[v || i++];
        });
    }

    exports.init = function(data) {
        patterns = data;
    }

    exports.resolve = function(name, args) {
        if (!patterns.hasOwnProperty(name)) {
            throw('URL pattern does not exist');
        }
        pattern = patterns[name];
        return interpolate(pattern, args);
    }

    return exports;
}());