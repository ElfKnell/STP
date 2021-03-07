export default {
    actions: {
        async fetchSection (ctx) {
            const response = await fetch('http://127.0.0.1:8000/api/v1/sections/all/');
            const ressect = await response.json();
            const sections = ressect.results;

            ctx.commit('updateSections', sections)
        }
    },
    mutations: {
        updateSections(state, sections) {
            state.sections = sections
        }
    },
    state: {
        sections: []
    },
    getters: {
        allSections(state) {
            return state.sections
        }
    }
}