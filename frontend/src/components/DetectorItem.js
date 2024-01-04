import {useState} from "react";
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';

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

function DetectorItem({ elem, num, activeStatus, setActiveStatus, data}) {
    const [editableMin, setEditableMin] = useState(false);
    const [editableMax, setEditableMax] = useState(false);
    const [elementMin, setElementMin] = useState(elem.min);
    const [elementMax, setElementMax] = useState(elem.max);

    function changeStatusMin(status) {
        setActiveStatus(status)
        setEditableMin(status)
    }

    function changeStatusMax(status) {
        setActiveStatus(status)
        setEditableMax(status)
    }

    function handleChangeMin(event) {
        setElementMin(event.target.value);
        if (event.target.value === ""
            || Number(event.target.value) > Number(elementMax)
            || (event.target.value.toString().indexOf(".") !== -1 && (event.target.value.toString().length <= 2 || event.target.value.toString()[0] === "." || event.target.value.toString()[event.target.value.toString().length - 1] === "0"))
            || (event.target.value.toString().indexOf(",") !== -1 && (event.target.value.toString().length <= 2 || event.target.value.toString()[0] === "," || event.target.value.toString()[event.target.value.toString().length - 1] === "0"))
            || (event.target.value.toString().length >= 2 && event.target.value.toString()[1] !== "," && event.target.value.toString()[1] !== "." && event.target.value.toString()[0] === 0..toString())
            || (event.target.value.toString().indexOf("-") !== -1 && ((event.target.value.toString().length === 2 && event.target.value.toString()[1] === "0") || (event.target.value.toString()[1] === "0" && event.target.value.toString()[2] !== "." && event.target.value.toString()[2] !== ",")))) {
            setValidatedMin(false);
        } else {
            setValidatedMin(true);
        }
    }

    function handleChangeMax(event) {
        setElementMax(event.target.value);
        if (event.target.value === ""
            || Number(event.target.value) < Number(elementMin)
                || (event.target.value.toString().indexOf(".") !== -1 && (event.target.value.toString().length <= 2 || event.target.value.toString()[0] === "." || event.target.value.toString()[event.target.value.toString().length - 1] === "0"))
            || (event.target.value.toString().indexOf(",") !== -1 && (event.target.value.toString().length <= 2 || event.target.value.toString()[0] === "," || event.target.value.toString()[event.target.value.toString().length - 1] === "0"))
                || (event.target.value.toString().length >= 2 && event.target.value.toString()[1] !== "," && event.target.value.toString()[1] !== "." && event.target.value.toString()[0] === 0..toString())
            || (event.target.value.toString().indexOf("-") !== -1 && ((event.target.value.toString().length === 2 && event.target.value.toString()[1] === "0") || (event.target.value.toString()[1] === "0" && event.target.value.toString()[2] !== "." && event.target.value.toString()[2] !== ",")))) {
            setValidatedMax(false);
        } else {
            setValidatedMax(true);
        }
    }

    const [validatedMin, setValidatedMin] = useState(true);
    const [validatedMax, setValidatedMax] = useState(true);


    const inputComponentMin = (
        <InputGroup className="mb-3" >
            <Form.Control
                type="number"
                placeholder="Минимальное значение"
                onChange={handleChangeMin}
                value={elementMin}
                aria-label=""
                className={validatedMin ? "" : "is-invalid"}
            />
            <Button disabled={!validatedMin} type="submit" onClick={() => elementMin ? successChangeMin(): null } variant="outline-success">
                Сохранить
            </Button>{' '}
            <div className={"invalid-feedback"}>Введите корректное число, меньшее максимального значения</div>
        </InputGroup>
    )

    const inputComponentMax = (
        <InputGroup className="mb-3" >
            <Form.Control
                type="number"
                placeholder="Минимальное значение"
                onChange={handleChangeMax}
                value={elementMax}
                aria-label=""
                className={validatedMax ? "" : "is-invalid"}
            />
            <Button disabled={!validatedMax} type="submit" onClick={() => elementMax ? successChangeMax(): null } variant="outline-success">
                Сохранить
            </Button>
            <div className={"invalid-feedback"}>Введите корректное число, большее минимального значения</div>
        </InputGroup>
    )

    const myStyle = {
        display: "flex",
        alignItems: "center"
    }
    const child = {
        marginRight: 10
    }


    function activeStatusError() {
        const errorMinBox = document.getElementById("textMin");
        const errorMin = document.createElement("div");
        errorMin.className = "invalid-feedback";
        errorMin.innerHTML = "Введите число";
        errorMinBox.appendChild(errorMin)
    }

    const textComponentMin = (
        <div id="textMin" style={myStyle}>
            <Button type="submit" size="sm" style={{marginRight: "12px"}} onClick={() => !activeStatus ? changeStatusMin(true): activeStatusError()} variant="outline-info">
                Изменить
            </Button>{' '}
            <div style={child}>{elementMin}</div>
        </div>
    )

    const textComponentMax = (
        <div style={myStyle}>
            <Button type="submit" size="sm" style={{marginRight: "12px"}} onClick={() => !activeStatus ? changeStatusMax(true): activeStatusError()} variant="outline-info">
                Изменить
            </Button>{' '}
            <div style={child}>{elementMax}</div>
        </div>
    )

    function successChangeMin() {
        changeStatusMin(false)
        data[num-1].min = elementMin
    }

    function successChangeMax() {
        changeStatusMax(false)
        data[num-1].max = elementMax
    }

    return (
        <tr>
            <td>{num}</td>
            <td>{incidentProp.types[elem.name] + ", " + incidentProp.units[elem.name]}</td>
            <td>{editableMin ? inputComponentMin : textComponentMin}</td>
            <td>{editableMax ? inputComponentMax : textComponentMax}</td>
        </tr>
    );
}

export default DetectorItem;