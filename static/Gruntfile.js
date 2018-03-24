module.exports = function (grunt) {
    // Project configuration.
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        coffee: {
            compile: {
                expand: true,
                flatten: true,
                src: ['coffee/*.coffee'],
                dest: './js',
                ext: '.js'
            }
        },
        watch: {
            scripts: {
                files: ['**/*.coffee'],
                tasks: ['coffee'],
                options: {
                    spawn: false
                }
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-coffee');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.registerTask('default', ['coffee']);
};