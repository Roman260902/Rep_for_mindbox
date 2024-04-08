from pyspark.sql.functions import col, lit, array_except


def get_product_category(spark, products_df, categories_df):

    product_category_pairs_df = products_df.crossJoin(categories_df)

    product_category_pairs_df = product_category_pairs_df.withColumn(
        "product_category_pair",
        col("product_name") + lit(" - ") + col("category_name")
    )

    products_with_no_categories_df = products_df.select("product_name").subtract(
        product_category_pairs_df.select("product_name")
    )

    result_df = product_category_pairs_df.select("product_category_pair").union(
        products_with_no_categories_df.withColumn(
            "product_category_pair", lit(None))
    )

    return result_df
