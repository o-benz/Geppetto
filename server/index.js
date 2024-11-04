const express = require('express');
const { exec } = require('child_process');
const app = express();
const port = 3000;

app.use(express.json());

app.post('/api/run-model', (req, res) => {
  const feature = req.body.feature;
  const company = req.body.company;
  const year = req.body.year;
  const file = req.body.file;
  let command;
  if (feature === '1') {
    command = `python ../scripts/summaryV2.py "${company}" "${year}" "${file}"`;
  } else if (feature === '2') {
    command = `python ../scripts/analysesdesentiment.py "${company}" "${year}" "${file}"`;
  } else if (feature === '3') {
    command = `python ../scripts/script3.py "${company}" "${year}" "${file}"`;
  } else {
    return res.status(400).send('Invalid feature value');
  }

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