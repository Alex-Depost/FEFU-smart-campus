import Table from 'react-bootstrap/Table';
import DetectorItem from "./DetectorItem";
import {useState} from "react";

function DetectorTable({data}) {
    const [activeStatus, setActiveStatus] = useState(false)
    const listItems = data.map((obj, number) =>
        <DetectorItem elem={obj} num={number + 1} key={number} activeStatus={activeStatus} setActiveStatus={setActiveStatus} data={data} />
    );
    return (
        <Table striped hover>
            <thead>
            <tr>
                <th>#</th>
                <th>Показатель</th>
                <th>Минимальное значение</th>
                <th>Максимальное значение</th>
            </tr>
            </thead>
            <tbody>
            {listItems}
            </tbody>
        </Table>
    );
}

export default DetectorTable;