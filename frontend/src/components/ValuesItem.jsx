import SubItems from "./SubItems";
import IncidentItem from "./IncidentItem";

function ValuesItem({ device, record }) {
    const dateTime = record.timestamp.slice(0, 10) + " " + record.timestamp.slice(11, 19);
    return (
        <tr>
            <td className="text-center">{device.name}</td>
            <td className="text-center">{dateTime}</td>
            <td className="text-center">{record.temp}</td>
            <td className="text-center">{record.co2}</td>
            <td className="text-center">{record.hum}</td>
            <td className="text-center">{record.noise}</td>
            <td className="text-center">{record.lux}</td>
        </tr>
    );
}

export default ValuesItem