const express = require('express');
const { exec } = require('child_process');
const app = express();
const port = 3000;

app.use(express.json());

app.post('/api/run-model', (req, res) => {
  const prompt = req.body.prompt;
  const command = `python ../scripts/rag.py "${prompt}"`;

  exec(command, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error executing script: ${error}`);
      console.error(`stderr: ${stderr}`);
      return res.status(500).send(`Error executing script: ${stderr}`);
    }
    console.log(`stdout: ${stdout}`);
    console.error(`stderr: ${stderr}`);
    res.json({ result: stdout });
  });
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});