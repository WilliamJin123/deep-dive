const path = require('path');

module.exports = {
    "entry": "./src/index.js",
    "output": {
        "filename": "bundle.js",
        "path": path.resolve(__dirname, 'dist'),
        "publicPath": '/',
    },
    "mode": "development",
    "devServer": {
        "static": {
            "directory": path.join(__dirname, './'),
        },
        "port": 8080, // You can choose any available port
        "open": true, // Automatically open the browser when the server starts
        "hot": true, // Enable Hot Module Replacement (HMR) for instant updates
        "compress": true, // Enable gzip compression for everything served
        "historyApiFallback": true, // Useful for SPAs, redirects 404s to index.html
    },
    "watchOptions": {
        "poll": 500
    }
}