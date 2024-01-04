import Form from 'react-bootstrap/Form';
import {Row} from "react-bootstrap";

function SwitchExample() {
    return (
        <Row xs="auto" className="justify-content-start m-1">
            <Form.Check
                style={{marginRight: "5%"}}
                type="switch"
                id="custom-switch"
                label="Включить кондиционер"
            />
            <Form.Check
                style={{marginRight: "5%"}}
                type="switch"
                id="custom-switch"
                label="Включить обогреватель"
            />
            <Form.Check
                style={{marginRight: "5%"}}
                type="switch"
                id="custom-switch"
                label="Включить вытяжку"
            />
            <Form.Check
                style={{marginRight: "5%"}}
                type="switch"
                id="custom-switch"
                label="Отключить напряжение"
            />
        </Row>
    );
}

export default SwitchExample;