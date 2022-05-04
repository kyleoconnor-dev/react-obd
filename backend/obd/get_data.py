import json
import obd

def get_conn():
    connection = obd.OBD()
    return connection

def get_data():

    conn = get_conn()

    cmds = {
            'speed': conn.commands.SPEED, 'rpm': conn.commands.RPM, 'coolant_temp': conn.commands.COOLANT_TEMP,
            'fuel_press': conn.commands.FUEL_PRESSURE, 'intake_temp': conn.commands.INTAKE_TEMP,
            'throttle_pos': conn.commands.THROTTLE_POS, 'load': conn.commands.ENGINE_LOAD,
            'maf': conn.commands.MAF, 'intake_press': conn.commands.INTAKE_PRESSURE, 'fuel_level': conn.commands.FUEL_LEVEL,
            'fuel_rate': conn.commands.FUEL_RATE, 'timing': conn.commands.TIMING_ADVANCE
        }
        

    resp = {key: conn.query(cmd) for key, cmd in cmds.items()}

    return json.dumps(resp)

if __name__ == '__main__':
    conn = get_conn()
    # Get rfcomm connection working to access data