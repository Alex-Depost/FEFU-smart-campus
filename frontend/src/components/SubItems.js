function SubItems({detectorValue, i, j}) {
    const isoDate = new Date(detectorValue.sensors[i].records[j].time * 1000).toISOString();
    const dateTime = isoDate.slice(0, 10) + " " + isoDate.slice(11, 19);
    return (
        <tr>
            <td className="text-center">{detectorValue.sensors[i].device_name}</td>
            <td className="text-center">{detectorValue.name}</td>
            <td className="text-center">{dateTime}</td>
            <td className="text-center">{detectorValue.sensors[i].records[j].temp}</td>
            <td className="text-center">{detectorValue.sensors[i].records[j].co2}</td>
            <td className="text-center">{detectorValue.sensors[i].records[j].hum}</td>
            <td className="text-center">{detectorValue.sensors[i].records[j].noise}</td>
            <td className="text-center">{detectorValue.sensors[i].records[j].lux}</td>
        </tr>
    );
}

export default SubItems