import { LineWave } from "react-loader-spinner";

function Loader() {
  return   <LineWave
    visible={true}
    height="200"
    width="100"
    color="#"
    ariaLabel="line-wave-loading"
    wrapperStyle={{}}
    wrapperClass=""
    firstLineColor=""
    middleLineColor=""
    lastLineColor=""
    />
}

export default Loader;