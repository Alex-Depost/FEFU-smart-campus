import {Table} from "react-bootstrap";
import IncidentItem from "./IncidentItem";
import {useEffect, useState} from "react";

function ArchiveTable() {
    const [items, setItems] = useState([]);
    function fetchData() {
        function compareByState(a, b) {
            return (a.status === "active") < (b.status === "active") ? 1 : -1;
        }

        return fetch("http://10.61.31.15:8000/api/sensors").then((response) => {
            return response.json()
        }).then((payload) => {
            payload.sort(compareByState);
            return payload;
        })
    }

    const handleClick = () => {
        fetchData().then((data) => setItems(data));
    };

    useEffect(() => {
        handleClick();
    }, []);

    const incidents = items.map((incident) =>  <IncidentItem incident={incident} handleClick={handleClick} key={incident.id}/>);

    return (
        <Table responsive hover bordered>
            <thead>
            <tr>
                <th className="text-center">Датчик</th>
                <th className="text-center">Локация</th>
                <th className="text-center">Дата и время</th>
                <th className="text-center">Показатель</th>
                <th className="text-center">Значение</th>
                <th className="text-center">Нормальный диапазон</th>
            </tr>
            </thead>
            <tbody>
                {incidents}
            </tbody>
        </Table>
    );
}

export default ArchiveTable;