const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

app.use(express.json());

// Emergency beacon signal endpoint
app.post('/beacon', (req, res) => {
  const { vessel_id, coordinates, signal_type } = req.body;
  
  console.log(`[DISTRESS] Beacon signal received from vessel ${vessel_id}`);
  console.log(`[LOCATION] Coordinates: ${coordinates}`);
  console.log(`[TYPE] Signal type: ${signal_type}`);
  
  // In production, this would relay to AWS Lambda
  res.json({
    status: 'received',
    message: 'Distress signal relayed to rescue coordination',
    vessel_id: vessel_id,
    relay_status: 'ACTIVE'
  });
});

// Health check
app.get('/health', (req, res) => {
  res.json({
    status: 'operational',
    frequency: '121.5MHz',
    monitoring: true
  });
});

app.listen(port, () => {
  console.log(`Emergency Beacon Relay listening on port ${port}`);
  console.log(`Monitoring frequency: 121.5MHz`);
  console.log(`Emergency channel: 16`);
});
