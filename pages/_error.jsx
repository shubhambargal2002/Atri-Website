/**
 *
 * @param {{statusCode: number}} props
 */
export default function (props) {
    return <div style={{ color: "#ef4444" }}>Error: {props.statusCode}</div>;
}
