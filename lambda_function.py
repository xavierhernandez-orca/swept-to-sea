import json
import os

def lambda_handler(event, context):
    """
    Emergency Beacon Relay System
    Processes distress signals from vessels swept to sea
    """
    
    # Get configuration from environment
    beacon_freq = os.environ.get('BEACON_FREQUENCY', '121.5MHz')
    emergency_channel = os.environ.get('EMERGENCY_CHANNEL', '16')
    relay_endpoint = os.environ.get('RELAY_ENDPOINT', 'unknown')
    
    # Parse incoming beacon signal
    try:
        body = json.loads(event.get('body', '{}'))
        signal_type = body.get('type', 'UNKNOWN')
        vessel_id = body.get('vessel_id', 'UNKNOWN')
        coordinates = body.get('coordinates', 'UNKNOWN')
        
        # Simulate beacon relay
        response = {
            'status': 'RELAYED',
            'signal_type': signal_type,
            'vessel_id': vessel_id,
            'coordinates': coordinates,
            'relay_frequency': beacon_freq,
            'emergency_channel': emergency_channel,
            'message': f'Distress signal from {vessel_id} relayed to maritime rescue services'
        }
        
        return {
            'statusCode': 200,
            'body': json.dumps(response),
            'headers': {
                'Content-Type': 'application/json',
                'X-Beacon-Status': 'ACTIVE'
            }
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'status': 'ERROR',
                'message': f'Beacon relay failed: {str(e)}'
            })
        }
