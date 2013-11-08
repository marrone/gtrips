module.exports = function(grunt) {

    "use strict";
    require("matchdep").filterDev("grunt-*").forEach(grunt.loadNpmTasks);

    grunt.initConfig({

        pkg: grunt.file.readJSON("package.json"),

        htmlhint: {
            build: {
                options: {
                    'tag-pair': true,
                    'tagname-lowercase': true,
                    'attr-lowercase': true,
                    'attr-value-double-quotes': true,
                    'doctype-first': true,
                    'spec-char-escape': true,
                    'id-unique': true,
                    'head-script-disabled': true,
                    'style-disabled': true
                },
                src: ['index.html']
            }
        },

        uglify: {
            build: {
                files: {
                    'build/js/app.min.js': [
                        "assets/js/lib/jquery.min.js",
                        "assets/js/lib/jquery-ui-1.10.3.custom.min.js",
                        "assets/js/lib/jquery.dateFormat-1.0.js",
                        "assets/js/lib/underscore-min.js",
                        "assets/js/app.js"
                    ]
                }
            }
        },

        react: {
            options: {
                extension: 'jsx',
                ignoreMTime: false
            },
            app: {
                files: {
                    'assets/js/views': 'assets/jsx/views'
                }
            },
        },

        cssc: {
            build: {
                options: {
                    consolidateViaDeclarations: false,
                    consolidateViaSelectors:    false,
                    consolidateMediaQueries:    false
                },
                files: {
                    'build/css/app.css': 'build/css/app.css'
                }
            }
        },

        cssmin: {
            build: {
                src: 'build/css/app.css',
                dest: 'build/css/app.css'
            }
        },

        compass: {
            dist: {
                options: {
                    config: 'config.rb'
                }
            }
        },

        watch: {
            js: {
                files: ['assets/js/**/*.js'],
                tasks: ['uglify']
            },
            css: {
                files: ['assets/sass/**/*.scss'],
                tasks: ['buildcss']
            }
        }
    });

    grunt.registerTask("default", []);
    grunt.registerTask('buildcss',  ['compass', 'cssc', 'cssmin']);

};
