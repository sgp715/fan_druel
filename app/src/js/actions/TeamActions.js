import dispatcher from "../dispatcher.js";

export function createTeam(team) {
    dispatcher.dispatch({
        type: "CREATE_TEAM",
        team: team
    })
}
