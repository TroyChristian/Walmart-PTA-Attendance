const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    mode: 'development',
    entry: {
        main: path.resolve(__dirname, 'assets/js/index.js'),
    },
    output: {
        path: path.resolve(__dirname, 'static', 'webpack_bundles'),
        filename: '[name]-[hash].js',
        clean: true,
        publicPath: '/static/webpack_bundles/',
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
            path: __dirname,  // Just the base directory
            filename: 'webpack-stats.json'  // Only the filename, no path segments
        }),
    ],
    resolve: {
        extensions: ['.js', '.jsx', '.css']
    }
};