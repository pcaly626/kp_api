const path = require('path');

module.exports = {
    module:{
        rules:[
            {
                test: /\.js$|\.tsx$|\.ts$/,
                exclude: /node_moduldes/,
                use:{
                    loader: "babel-loader"
                }
            },
            {
                test: /\.css$/,
                use: [
                    'style-loader',
                    'css-loader'
                ]
            }     
        ]
    }
}