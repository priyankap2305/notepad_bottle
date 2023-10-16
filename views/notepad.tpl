<!DOCTYPE html>
<html>

<head>
    <title>Notepad</title>
</head>

<body>
    <h1>Notepad</h1>
    <textarea id="notepad" rows="10" cols="50"></textarea><br>
    <button onclick="saveNote()">Save Note</button>
    <div id="message"></div>

    <script>
        function saveNote() {
            var note = document.getElementById("notepad").value;
            fetch('/save', {
                    method: 'POST',
                    body: JSON.stringify({
                        note: note
                    }),
                    headers: {
                        'Content-Type': 'application/json'
                    }
                })
                .then(response => response.json())
                .then(data => {
                    document.getElementById("message").innerHTML = data.message;
                })
                .catch(error => console.error('Error:', error));
        }
    </script>
</body>

</html>