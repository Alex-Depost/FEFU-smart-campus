import {Button} from "react-bootstrap";
import {useState} from "react";
import {API_URL} from "../variables";

const incidentProp = {
    types: {
        temp: "Температура",
        co2: "CO₂",
        hum: "Влажность",
        noise: "Шум",
        lux: "Освещение"
    },
    units: {
        temp: "℃",
        co2: "ppm",
        hum: "%",
        noise: "дБ",
        lux: "лк"
    }
}

const normalValuesIndexes = {
    temp: 0,
    co2: 1,
    hum: 2,
    lux: 3,
    noise: 4
}

function IncidentItem({ incident, handleClick, normalValues, idx }) {
    const [isActive, setIsActive] = useState(incident.status === "active");
    async function changeStateRequest() {
        incident.status = incident.status === "active" ? "fixing" : "active";
        await fetch(API_URL + "/incidents/" + incident.id, {
            method: "PATCH",
            body: JSON.stringify({status: incident.status}),
            headers: {
                'Content-Type': 'application/json'
            },
        })
    }

    async function changeState(active) {
        if (active !== isActive) {
            await changeStateRequest()
            setIsActive(active);
            handleClick();
        }
    }

    const dateTime = incident.timestamp.slice(0, 10) + " " + incident.timestamp.slice(11, 19);
    
    return (
        <tr key={incident.id}>
            <td className="text-center">{incident.device.name}</td>
            <td className="text-center">{incident.device.audience.name}</td>
            <td className="text-center">{dateTime}</td>
            <td className="text-center">{incidentProp.types[incident.type]}</td>
            <td className="text-center">{incident.value + " " + incidentProp.units[incident.type]}</td>
            <td className="text-center">
                {normalValues[normalValuesIndexes[incident.type]].min + " ‒ "
                    + normalValues[normalValuesIndexes[incident.type]].max + " "
                    + incidentProp.units[incident.type]}</td>
            <td className="text-center">{incident.status === "critical" ? "🚨 критическая" : "⚠ предупреждение"}</td>
            <td className="text-center"><Button variant={isActive ? "danger" : "outline-danger"} className={"mx-3"} size="sm" onClick={() => changeState(true)}>Активна</Button>{' '}
                <Button variant={isActive ? "outline-warning" : "warning"} className={"m-1"} size="sm" onClick={() => changeState(false)}>Устраняется</Button>{' '}</td>
        </tr>
    );
}

export default IncidentItem