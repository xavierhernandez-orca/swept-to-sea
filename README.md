# Emergency Beacon Relay System

A maritime emergency beacon relay system that processes and forwards distress signals from vessels in danger.

## Overview

This system acts as a relay station for emergency beacons (EPIRB/PLB) operating on international distress frequencies. When a vessel is swept to sea or encounters an emergency, their beacon signal is received, processed, and relayed to maritime rescue coordination centers.

## Features

- 🚨 Real-time distress signal processing
- 📡 Multi-frequency beacon monitoring (121.5MHz, 406MHz)
- 🌊 Automatic position tracking
- 🆘 Emergency channel coordination
- ☁️ Serverless architecture on AWS Lambda

## Architecture

The system consists of:
- **Node.js Signal Processor**: Receives and validates incoming beacon signals
- **AWS Lambda Backend**: Processes and relays validated signals to rescue services
- **Automated Deployment**: GitHub Actions workflow for configuration updates

## Deployment

Configuration changes are automatically deployed via GitHub Actions:

1. Update beacon frequencies or relay endpoints in the repository
2. Manually trigger the deployment workflow
3. Configuration is synchronized to the Lambda function

## Environment Variables

The Lambda function uses the following configuration:
- `BEACON_FREQUENCY`: Primary monitoring frequency
- `EMERGENCY_CHANNEL`: VHF emergency channel number
- `RELAY_ENDPOINT`: Rescue coordination center endpoint
- `RESCUE_COORDINATES`: Default rescue staging coordinates

