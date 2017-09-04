var path = require("path")
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')

var dist_dir = '/static/dist';
// Controls use of hot-reload devserver. When this is used you must also run `node server.js`
var use_hot_reload = process.env.NODE_ENV !== 'production';
// Dev server address specified in server.js
var dev_server_addr = 'localhost';
// Dev server port specified in server.js
var dev_server_port = 8001;


module.exports = {
context: __dirname,

entry: './assets/js/index.home.js',

output: {
    path: path.resolve('./assets/bundles/'),
    filename: "[name]-[hash].js",
},

plugins: [
    new BundleTracker({filename: './webpack-stats.json'}),
],

 module: {
        rules: [
            {
                test: /\.vue$/,
                loader: 'vue-loader',
                options: {
                    loaders: {
                        // Since sass-loader (weirdly) has SCSS as its default parse mode, we map
                        // the "scss" and "sass" values for the lang attribute to the right configs here.
                        // other preprocessors should work out of the box, no loader config like this nessessary.
                        'scss': 'vue-style-loader!css-loader!sass-loader',
                        'sass': 'vue-style-loader!css-loader!sass-loader?indentedSyntax'
                    }
                    // other vue-loader options go here
                }
            },
            {
                test: /\.js$/,
                loader: 'babel-loader',
                exclude: /node_modules/
            },
            {
                test: /\.(png|jpg|gif|svg)$/,
                loader: 'file-loader',
                options: {
                    name: '[name].[ext]?[hash]'
                }
            }
        ]
    },
    resolve: {
        alias: {
            'vue$': 'vue/dist/vue.common.js'
        }
    },
    devServer: {
        historyApiFallback: true,
        noInfo: true
    },
    performance: {
        hints: false
    },
    devtool: '#eval-source-map'
};

if (process.env.NODE_ENV === 'production')
{
    module.exports.devtool = '#source-map'
    // http://vue-loader.vuejs.org/en/workflow/production.html
    module.exports.plugins = (module.exports.plugins || []).concat([
        new webpack.DefinePlugin({
            'process.env': {
                NODE_ENV: '"production"'
            }
        }),
        new webpack.optimize.UglifyJsPlugin({
            sourceMap: true,
            compress: {
                warnings: false
            }
        }),
        new webpack.LoaderOptionsPlugin({
            minimize: true
        })
    ])
}
else if (use_hot_reload)
{
    module.exports.entry.push('webpack-dev-server/client?http://' + dev_server_addr + ':' + dev_server_port);
    module.exports.entry.push('webpack/hot/only-dev-server');
    module.exports.output['publicPath'] = 'http://' + dev_server_addr + ':' + dev_server_port + dist_dir + '/';
    module.exports.plugins.push(new webpack.HotModuleReplacementPlugin());
    module.exports.plugins.push(new webpack.NoEmitOnErrorsPlugin()); // don't reload if there is an error
}

}