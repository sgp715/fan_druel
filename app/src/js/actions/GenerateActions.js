import dispatcher from "../dispatcher.js";

export function toggleGenerate() {
    dispatcher.dispatch({
        type: "TOGGLE_GENERATE"
    })
}
