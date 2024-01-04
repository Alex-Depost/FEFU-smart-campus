import 'bootstrap/dist/css/bootstrap.min.css';
import IncidentsTable from "../components/IncidentsTable";
import {Card, Container} from "react-bootstrap";
import DetectorTable from "../components/DetectorTable";
import {useEffect, useState} from "react";
import {API_URL} from "../variables";

function Incidents() {
    const [normalValues, setNormalValues] = useState([]);
    function fetchNormalValues() {
        return fetch(API_URL + "/normal_values").then((response) => {
            return response.json();
        }).then((payload) => {
            return payload;
        })
    }

    useEffect(() => {
        fetchNormalValues().then((data) => setNormalValues(data));
    }, []);

    return (
        <Container fluid className={"mt-3"}>
            <Card shadow={"true"} className={"mb-3 ml-1"}>
                <Card.Header flex={"true"} className="text-center h3">Список инцидентов на данный момент</Card.Header>
                <IncidentsTable normalValues={normalValues} />
                {/*<ValuesTable />*/}
            </Card>
            <Card shadow={"true"} className={"mb-3 ml-1"}>
                <Card.Header className="d-flex justify-content-center h3">Допустимые значения показателей</Card.Header>
                <DetectorTable data={normalValues} />
            </Card>
        </Container>
    );
}

export default Incidents;
