import Card from 'react-bootstrap/Card';
import ListGroup from 'react-bootstrap/ListGroup';
import Button from "react-bootstrap/Button";
import {Col} from "react-bootstrap";
import {Link} from "react-router-dom";

function AudienceCard({ audience }) {
    return (
        <Col className="mb-3">
            <Card style={{ width: '15rem' }}>
                <Card.Body>
                    <Card.Title style={{ height: '2rem' }}>{audience.name}</Card.Title>
                </Card.Body>
                <ListGroup className="list-group-flush">
                    <ListGroup.Item>Площадь: {audience.floor_space}</ListGroup.Item>
                    <ListGroup.Item>Напряжение: {audience.voltage}</ListGroup.Item>
                    <ListGroup.Item>Расположение: {audience.location}</ListGroup.Item>
                </ListGroup>
                <Card.Body>
                    <Link to={`${audience.id}`}>
                        <Button variant={"outline-secondary"} className={"mx-3"}>перейти</Button>
                    </Link>
                </Card.Body>
            </Card>
        </Col>
    );
}

export default AudienceCard;