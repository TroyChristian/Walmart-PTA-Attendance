// webpack.config.js
const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    mode: 'development',  // Change to 'production' for production builds
    entry: {
        main: 'tracker/assets/js/index.js',
    },
    output: {
        path: path.resolve('tracker/static/webpack_bundles/'),
        filename: '[name]-[hash].js',
        clean: true,
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env']
                    }
                }
            },
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader'],
            }
        ]
    },
    plugins: [
        new BundleTracker({
            path: __dirname,
            filename: './webpack-stats.json'
        }),
    ]
};
