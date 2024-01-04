import {Table} from "react-bootstrap";
import {useEffect, useState} from "react";
import ValuesItem from "./ValuesItem";

function ValuesTable({ devices }) {
    const [records, setRecords] = useState([])

    useEffect(() => {
        if (devices) {
            setRecords(
                devices.map((device) => {
                    return device.records.map((record) => {
                        return <ValuesItem key={record.id} device={device} record={record}/>
                    })
                })
            );
        }
    }, [devices]);

    return (
        <Table responsive hover bordered>
            <thead>
            <tr>
                <th className="text-center">Датчик</th>
                <th className="text-center">Время получения данных</th>
                <th className="text-center">Температура, ℃</th>
                <th className="text-center">CO₂, ppm</th>
                <th className="text-center">Влажность, %</th>
                <th className="text-center">Шум, дБ</th>
                <th className="text-center">Освещение, лк</th>
            </tr>
            </thead>
            <tbody>
                {records}
            </tbody>
        </Table>
    );
}

export default ValuesTable;