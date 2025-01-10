setImmediate(function() {
    Java.use("").onCreate.implementation = function(x) {
        console.log("demo.js: onCreate() called");
        return this.onCreate(x);
    }
})