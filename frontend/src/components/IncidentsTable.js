import {Table} from "react-bootstrap";
import IncidentItem from "./IncidentItem";
import {useEffect, useState} from "react";
import { API_URL } from "../variables"

function IncidentsTable({normalValues}) {
    const [items, setItems] = useState([]);
    function fetchData() {
        function compareByState(a, b) {
            return (a.status === "active") < (b.status === "active") ? 1 : -1; //
        }

        return fetch(API_URL + "/incidents").then((response) => {
            return response.json();
        }).then((payload) => {
            payload.sort(compareByState);
            return payload;
        })
    }

    const handleClick = () => {
        fetchData().then((data) => setItems(data));
    };

    const incidents = items.map((incident, index) =>  <IncidentItem incident={incident} handleClick={handleClick} key={incident.id} normalValues={normalValues} idx={index}/>);

    function recursiveRequest() {
        fetchData();
        setTimeout(recursiveRequest, 300000);
    }

    setTimeout(recursiveRequest, 300000); // 300000

    useEffect(() => {
        handleClick();
    }, []);

    if (incidents.length || true) {

        return (
            <Table responsive hover bordered>
                <thead>
                <tr>
                    <th className="text-center">Датчик</th>
                    <th className="text-center">Локация</th>
                    <th className="text-center">Дата и время</th>
                    <th className="text-center">Показатель</th>
                    <th className="text-center">Текущее значение</th>
                    <th className="text-center">Нормальный диапазон</th>
                    <th className="text-center" id="status" scope="col">Тип угрозы</th>
                    <th className="text-center" id="status" scope="col">Состояние угрозы</th>
                </tr>
                </thead>
                <tbody>
                {incidents}
                </tbody>
            </Table>
        );
    } else {
        return (
            <p>На данный момент инцидентов нет!</p>
        )
    }
}

export default IncidentsTable;