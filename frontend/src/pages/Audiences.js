import AudienceCard from "../components/AudienceCard";
import {useEffect, useState} from "react";
import {Container, Row} from "react-bootstrap";
import { API_URL } from "../variables"
import {Outlet} from "react-router-dom";

function Audiences() {
    const [audiences, setAudiences] = useState([]);

    useEffect(() => {
        fetch(API_URL + "/audiences").then((response) => {
            return response.json();
        }).then((payload) => {
            setAudiences(payload);
        })
    }, []);

    const cards = audiences.map(audience => <AudienceCard audience={audience} key={audience.id} />);

    return (
        <Container fluid className="mt-3">
            <Outlet />
            <Row xs="auto" className="justify-content-center">
                {cards}
            </Row>
        </Container>
    )
}

export default Audiences