const express = require('express');
const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = 3000;

// Serve static files from the current directory
app.use(express.static(__dirname));

app.get('/run_algorithm', (req, res) => {
    const algorithm = req.query.algorithm;
    const array = req.query.array.split(',').map(Number);

    const algorithmFileName = `${algorithm}.py`;
    const algorithmFilePath = path.join(__dirname, 'algorithms', algorithmFileName);

    fs.access(algorithmFilePath, fs.constants.F_OK, (err) => {
        if (err) {
            console.error(`File not found: ${algorithmFilePath}`);
            return res.status(404).send({ error: 'Algorithm file not found' });
        }

        const pythonProcess = spawn('python3', [algorithmFilePath, ...array]);

        let visualization = '';
        let errorData = '';

        pythonProcess.stdout.on('data', (data) => {
            visualization += data.toString();
        });

        pythonProcess.stderr.on('data', (data) => {
            errorData += data.toString();
        });

        pythonProcess.on('close', (code) => {
            if (code !== 0) {
                res.status(500).send({ error: errorData });
                return;
            }

            fs.readFile(algorithmFilePath, 'utf8', (err, code) => {
                if (err) {
                    res.status(500).send({ error: 'Failed to read Python code file' });
                    return;
                }
                res.json({
                    visualization: visualization,
                    code: code
                });
            });
        });
    });
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
