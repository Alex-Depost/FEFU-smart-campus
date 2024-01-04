import ValuesTable from "../components/ValuesTable";
import {Card, Container} from "react-bootstrap";
import Switch from "../components/Switch";
import {useEffect, useState} from "react";
import {API_URL} from "../variables";
import {useParams} from "react-router-dom";

function AudienceInfo() {
    const { audienceId} = useParams();
    const [audience, setAudience] = useState()

    useEffect(() => {
        fetch(API_URL + "/audiences/" + audienceId).then((response) => {
            return response.json()
        }).then((audience) => {
            setAudience(audience);
        })
        window.scroll(0, 0)
    }, [audienceId]);

    return (
        <Card shadow={"true"} className={"mb-3 ml-1"}>
            <Card.Header flex={"true"} className="text-center h3" >{audience ? audience.name: "Датчик"}</Card.Header>
            <ValuesTable devices={audience ? audience.devices: []} />
            <Container fluid className={"mb-3"}>
                <Switch />
            </Container>
        </Card>
    )
}

export default AudienceInfo