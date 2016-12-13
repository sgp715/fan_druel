import dispatcher from "../dispatcher.js";

export function createTeam() {
    dispatcher.dispatch({
        type: "CREATE_TEAM"
    })
}
