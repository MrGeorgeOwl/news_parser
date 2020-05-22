<template>
    <div>
        <Header></Header>
        <h1>News for today</h1>
        <b-container>
            <b-row>
                <b-col></b-col>
                <b-col cols="6">
                    <Article v-for="(article, index) in articles" :key="index" :articleData="article"></Article>
                </b-col>
                <b-col></b-col>
            </b-row>
        </b-container>
        <Footer></Footer>
    </div>
</template>

<script>
    import Article from "./Article"
    import Header from "./Header"
    import Footer from "./Footer"

    export default {
        components: {
            "Article": Article,
            "Header": Header,
            "Footer": Footer
        },
        name: "Home",
        props: {
            message: {
                type: String,
                required: false,
                default: "",
            }
        },
        data () {
            return {
                articles: []
            }
        },
        mounted(){
            fetch('http://localhost:8000/api/articles/?amount=10&sort_articles=1',
            {
                method: "get",
            })
            .then(response => {
                return response.json()
            })
            .then(json => this.articles = json)
        }
    }
</script>

<style scoped>

</style>
