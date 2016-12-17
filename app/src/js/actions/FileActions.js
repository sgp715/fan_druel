import dispatcher from "../dispatcher.js";

export function updateFile(file) {
    dispatcher.dispatch({
        type: "UPDATE_FILE",
        file: file
    });
}
