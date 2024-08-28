    document.getElementById('video').addEventListener('loadeddata', function() {
        this.play();
    }, false);


    document.getElementById('control-area').focus();

    let command = '';
    let status = document.getElementById('status');

    document.getElementById('control-area').addEventListener('keydown', function(event) {
        switch(event.key) {
            case 'e':
                command = 'e';
                status.textContent = 'Taking off...';
                break;
            case 'q':
                command = 'q';
                status.textContent = 'Landing...';
                break;
            case 'ArrowUp':
                command = 'UP';
                status.textContent = 'Moving Forward';
                break;
            case 'ArrowDown':
                command = 'DOWN';
                status.textContent = 'Moving Backward';
                break;
            case 'ArrowLeft':
                command = 'LEFT';
                status.textContent = 'Moving Left';
                break;
            case 'ArrowRight':
                command = 'RIGHT';
                status.textContent = 'Moving Right';
                break;
            case 'w':
                command = 'w';
                status.textContent = 'Moving Up';
                break;
            case 's':
                command = 's';
                status.textContent = 'Moving Down';
                break;
            case 'a':
                command = 'a';
                status.textContent = 'Rotating Left';
                break;
            case 'd':
                command = 'd';
                status.textContent = 'Rotating Right';
                break;
            case 'g':
                command = 'g';
                status.textContent = 'Back Flipping     ';
                break;
            default:
                command = '';
                status.textContent = 'Key not recognized';
        }

        if (command) {
            $.ajax({
                url: '/drone/control/',
                method: 'POST',
                data: {
                    command: command,
                    csrfmiddlewaretoken: '{{ csrf_token }}'
                },
                success: function(response) {
                    console.log('Command sent:', command);
                },
                error: function(error) {
                    console.log('Error sending command:', error);
                }
            });
        }
    });

    document.getElementById('control-area').addEventListener('keyup', function(event) {
        // Stop the drone when key is released
        $.ajax({
            url: '/drone/control/',
            method: 'POST',
            data: {
                command: 'STOP',
                csrfmiddlewaretoken: '{{ csrf_token }}'
            },
            success: function(response) {
                status.textContent = 'Stopped';
                console.log('Command sent: STOP');
            },
            error: function(error) {
                console.log('Error sending stop command:', error);
            }
        });
    });