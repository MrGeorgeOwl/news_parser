<template>
    <div>
        <b-container class="article-class">
            <b-row>
                <b-col cols="9">
                    <p>{{ article.title }}</p>
                </b-col>
                <b-col>
                    <img :src="article.image_link">
                </b-col>
            </b-row>
            <b-row style="margin-top: 6px;">
                <b-col>
                    <a :href="article.url" style="margin-right: 10px">{{ article.author }}</a>
                    {{ computed_date }}
                </b-col>
            </b-row>
        </b-container>
    </div>
</template>

<script>
export default {
    props: ["articleData"],
    data () {
        return {
            article: this.articleData
        }
    },
    computed: {
        computed_date() {
            let now = new Date();
            let article_date = new Date(this.article.created_at);
            let timestamp =  now - article_date;
            return this.buildDateString(this.calculateTimestamp(timestamp))
        }
    },
    methods: {
        calculateTimestamp(timestampInMillseconds) {
            return {
                days: timestampInMillseconds / 1000 / 86400,
                hours: timestampInMillseconds / 1000 /3600,
                minutes: timestampInMillseconds / 1000 /60,
            }
        },
        buildDateString(timestampObj){
            for (let key in timestampObj){
                if (timestampObj[key] > 0) {
                    return Math.floor(timestampObj[key]) + " " + key + " ago";
                }
            }
        }
    }
}
</script>

<style scoped>
img {
    height: 50px;
}
.article-class {
    text-align: left;
    padding: 20px;
    height: 200px;
    border: solid 1px black;
    border-radius: 10px;
    margin-bottom: 20px;
}
</style>