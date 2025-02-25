####################################### Model Table Column Name ########################################


############################################### Fields #################################################
htmlfields = {
    'que1': {'Q1: is_the_context_link_valid': ['Yes', 'No']},
    'que2': {'Q2: do_you_understand_the_query': ['Yes', 'No']},
    'que3': {'Q3: what_is_the_query_type': [
        'Broad Query - Category/Brand List', 'Broad Query - Key Consideration',
        'Broad Query - General Knowledge Question', 'Search Keyword', 'Product Recommendation',
        'Comparison', 'Product Questions - Factoid', 'Product Questions - Review', 'Order History',
        'About Amazon - Broad', 'About Amazon - General Q&A', 'About Amazon - Issues', 'Other/Non-Shopping'
    ]},
    'que4': {'Q4: what_is_the_query_category': [
        'Hardlines', 'Softlines', 'Consumables', 'Media and Editorial', 'Multi-Category',
        'Amazon Devices', 'Amazon Programs', 'Amazon Services', 'Amazon Issues',
        'Amazon Destinations', 'Other'
    ]},
    'que5_ans1': {'Q5: does_the_response_contain_a_text_based_answer? Answer 1': ['Yes', 'No']},
    'que6_ans1': {'Q6: is_the_text_response_free_of_sensitive_content? Answer 1': ['Yes', 'No', 'Unsure']},
    'que6a_ans1': {'Q6A: select_the_dimension_that_was_violated_text_response? Answer 1': ['commercially_sensitive', 'offensive_content', 'professional_advice', 'privacy']},
    'que6a1_ans1': {'Q6A1: select_the_sub_dimension_that_was_violated_commercially_sensitive? Answer 1': [
        'proc', 'product_usage_and_safety', 'product_reviews_and_ratings', 'product_description',
        'brand damaging', 'counterfeit_products', 'pricing', 'delivery_times_and_policies',
        'return_policies', 'sensitive_business_information', 'green_marketing', 'copyright', 'persona'
    ]},
    'que6a2_ans1': {'Q6A2: select_the_sub_dimension_that_was_violated_offensive_content? Answer 1': [
        'minor_protection_controlled_substances', 'minor_protection_adult_and_sexual_products',
        'minor_protection_child_abuse_and_exploitation', 
        'profanity', 'hate_and_intolerance', 'human_and_animal_harm', 'illegal_activity',
        'sexual_content', 'sensitive_topics', 'unethical_content'
    ]},
    'que6a3_ans1': {'Q6A3: select_the_sub_dimension_that_was_violated_professional_advice? Answer 1': ['legal', 'medical', 'financial', 'food_safety']},
    'que6a4_ans1': {'Q6A4: select_the_sub_dimension_that_was_violated_privacy? Answer 1': ['Pii']},
    'que7_ans1': {'Q7: is_the_response_relevant_to_the_customers_query_in_the_context_of_the_conversation? Answer 1': ['Yes', 'Somewhat', 'No']},
    'que8_ans1': {'Q8: is_the_response_complete_without_any_missing_information? Answer 1': ['Yes', 'No']},
    'que26_ans1': {'Q26: does_the_response_contain_any_related_questions? Answer 1': ['Yes', 'No']},
    'que27_ans1': {'Q27: is_the_related_question_plausible? Answer 1': ['Yes', 'No']},
    'que28_ans1': {'Q28: is_the_related_question_free_of_sensitive_content? Answer 1': ['Yes', 'No', 'Unsure']},
    'que28a_ans1': {'Q28A: select_the_dimension_that_was_violated_related_question? Answer 1': ['commercially_sensitive', 'offensive_content', 'professional_advice', 'privacy']},
    'que28a1_ans1': {'Q28A1: select_the_sub_dimension_that_was_violated_commercially_sensitive? Answer 1': [
        'proc', 'product_usage_and_safety', 'product_reviews_and_ratings', 'product_description',
        'brand damaging', 'counterfeit_products', 'pricing', 'delivery_times_and_policies',
        'return_policies', 'sensitive_business_information', 'green_marketing', 'copyright', 'persona'
    ]},
    'que28a2_ans1': {'Q28A2: select_the_sub_dimension_that_was_violated_offensive_content? Answer 1': [
        'minor_protection_controlled_substances', 'minor_protection_adult_and_sexual_products',
        'minor_protection_child_abuse_and_exploitation', 
        'profanity', 'hate_and_intolerance', 'human_and_animal_harm', 'illegal_activity',
        'sexual_content', 'sensitive_topics', 'unethical_content'
    ]},
    'que28a3_ans1': {'Q28A3: select_the_sub_dimension_that_was_violated_professional_advice? Answer 1': ['legal', 'medical', 'financial', 'food_safety']},
    'que28a4_ans1': {'Q28A4: select_the_sub_dimension_that_was_violated_privacy? Answer 1': ['Pii']},
    'que29_ans1': {'Q29: General commands? Answer 1': []},
    
    'que5_ans2': {'Q5: does_the_response_contain_a_text_based_answer? Answer 2': ['Yes', 'No']},
    'que6_ans2': {'Q6: is_the_text_response_free_of_sensitive_content? Answer 2': ['Yes', 'No', 'Unsure']},
    'que6a_ans2': {'Q6A: select_the_dimension_that_was_violated_text_response? Answer 2': ['commercially_sensitive', 'offensive_content', 'professional_advice', 'privacy']},
    'que6a1_ans2': {'Q6A1: select_the_sub_dimension_that_was_violated_commercially_sensitive? Answer 2': [
        'proc', 'product_usage_and_safety', 'product_reviews_and_ratings', 'product_description',
        'brand damaging', 'counterfeit_products', 'pricing', 'delivery_times_and_policies',
        'return_policies', 'sensitive_business_information', 'green_marketing', 'copyright', 'persona'
    ]},
    'que6a2_ans2': {'Q6A2: select_the_sub_dimension_that_was_violated_offensive_content? Answer 2': [
        'minor_protection_controlled_substances', 'minor_protection_adult_and_sexual_products',
        'minor_protection_child_abuse_and_exploitation',
        'profanity', 'hate_and_intolerance', 'human_and_animal_harm', 'illegal_activity',
        'sexual_content', 'sensitive_topics', 'unethical_content'
    ]},
    'que6a3_ans2': {'Q6A3: select_the_sub_dimension_that_was_violated_professional_advice? Answer 2': ['legal', 'medical', 'financial', 'food_safety']},
    'que6a4_ans2': {'Q6A4: select_the_sub_dimension_that_was_violated_privacy? Answer 2': ['Pii']},
    'que7_ans2': {'Q7: is_the_response_relevant_to_the_customers_query_in_the_context_of_the_conversation? Answer 2': ['Yes', 'Somewhat', 'No']},
    'que8_ans2': {'Q8: is_the_response_complete_without_any_missing_information? Answer 2': ['Yes', 'No']},
    'que26_ans2': {'Q26: does_the_response_contain_any_related_questions? Answer 2': ['Yes', 'No']},
    'que27_ans2': {'Q27: is_the_related_question_plausible? Answer 2': ['Yes', 'No']},
    'que28_ans2': {'Q28: is_the_related_question_free_of_sensitive_content? Answer 2': ['Yes', 'No', 'Unsure']},
    'que28a_ans2': {'Q28A: select_the_dimension_that_was_violated_related_question? Answer 2': ['commercially_sensitive', 'offensive_content', 'professional_advice', 'privacy']},
    'que28a1_ans2': {'Q28A1: select_the_sub_dimension_that_was_violated_commercially_sensitive? Answer 2': [
        'proc', 'product_usage_and_safety', 'product_reviews_and_ratings', 'product_description',
        'brand damaging', 'counterfeit_products', 'pricing', 'delivery_times_and_policies',
        'return_policies', 'sensitive_business_information', 'green_marketing', 'copyright', 'persona'
    ]},
    'que28a2_ans2': {'Q28A2: select_the_sub_dimension_that_was_violated_offensive_content? Answer 2': [
        'minor_protection_controlled_substances', 'minor_protection_adult_and_sexual_products',
        'minor_protection_child_abuse_and_exploitation', 
        'profanity', 'hate_and_intolerance', 'human_and_animal_harm', 'illegal_activity',
        'sexual_content', 'sensitive_topics', 'unethical_content'
    ]},
    'que28a3_ans2': {'Q28A3: select_the_sub_dimension_that_was_violated_professional_advice? Answer 2': ['legal', 'medical', 'financial', 'food_safety']},
    'que28a4_ans2': {'Q28A4: select_the_sub_dimension_that_was_violated_privacy? Answer 2': ['Pii']},
    'que29_ans2': {'Q29: General commands? Answer 2': []}
}


#################################### Separate Columns l1,l2,l3,l4 #########################################

l1list = [
    'l1_status',
    'l1_emp_id__employeeID',
    'l1_emp_id__employeeName',
    'l1_emp_id__location',
    'l1_prod_id__start_time',
    'l1_prod_id__end_time',
    'l1_prod_id__end_time__date',

    'l1_prod_id__que1',
    'l1_prod_id__que2',
    'l1_prod_id__que3',
    'l1_prod_id__que4',

    'l1_prod_id__que5_ans1',
    'l1_prod_id__que6_ans1',
    'l1_prod_id__que6a_ans1',
    'l1_prod_id__que6a1_ans1',
    'l1_prod_id__que6a2_ans1',
    'l1_prod_id__que6a3_ans1',
    'l1_prod_id__que6a4_ans1',
    'l1_prod_id__que7_ans1',
    'l1_prod_id__que8_ans1',
    'l1_prod_id__que26_ans1',
    'l1_prod_id__que27_ans1',
    'l1_prod_id__que28_ans1',
    'l1_prod_id__que28a_ans1',
    'l1_prod_id__que28a1_ans1',
    'l1_prod_id__que28a2_ans1',
    'l1_prod_id__que28a3_ans1',
    'l1_prod_id__que28a4_ans1',

    'l1_prod_id__que5_ans2',
    'l1_prod_id__que6_ans2',
    'l1_prod_id__que6a_ans2',
    'l1_prod_id__que6a1_ans2',
    'l1_prod_id__que6a2_ans2',
    'l1_prod_id__que6a3_ans2',
    'l1_prod_id__que6a4_ans2',
    'l1_prod_id__que7_ans2',
    'l1_prod_id__que8_ans2',
    'l1_prod_id__que26_ans2',
    'l1_prod_id__que27_ans2',
    'l1_prod_id__que28_ans2',
    'l1_prod_id__que28a_ans2',
    'l1_prod_id__que28a1_ans2',
    'l1_prod_id__que28a2_ans2',
    'l1_prod_id__que28a3_ans2',
    'l1_prod_id__que28a4_ans2',

    'l1_prod_id__que29_ans1',
    'l1_prod_id__que29_ans2'
]


l4list = [
    'l4_status',
    'l4_emp_id__employeeID',
    'l4_emp_id__employeeName',
    'l4_emp_id__location',
    'l4_prod_id__start_time',
    'l4_prod_id__end_time',
    'l4_prod_id__end_time__date',

    'l4_prod_id__que1',
    'l4_prod_id__que2',
    'l4_prod_id__que3',
    'l4_prod_id__que4',

    'l4_prod_id__que5_ans1',
    'l4_prod_id__que6_ans1',
    'l4_prod_id__que6a_ans1',
    'l4_prod_id__que6a1_ans1',
    'l4_prod_id__que6a2_ans1',
    'l4_prod_id__que6a3_ans1',
    'l4_prod_id__que6a4_ans1',
    'l4_prod_id__que7_ans1',
    'l4_prod_id__que8_ans1',
    'l4_prod_id__que26_ans1',
    'l4_prod_id__que27_ans1',
    'l4_prod_id__que28_ans1',
    'l4_prod_id__que28a_ans1',
    'l4_prod_id__que28a1_ans1',
    'l4_prod_id__que28a2_ans1',
    'l4_prod_id__que28a3_ans1',
    'l4_prod_id__que28a4_ans1',

    'l4_prod_id__que5_ans2',
    'l4_prod_id__que6_ans2',
    'l4_prod_id__que6a_ans2',
    'l4_prod_id__que6a1_ans2',
    'l4_prod_id__que6a2_ans2',
    'l4_prod_id__que6a3_ans2',
    'l4_prod_id__que6a4_ans2',
    'l4_prod_id__que7_ans2',
    'l4_prod_id__que8_ans2',
    'l4_prod_id__que26_ans2',
    'l4_prod_id__que27_ans2',
    'l4_prod_id__que28_ans2',
    'l4_prod_id__que28a_ans2',
    'l4_prod_id__que28a1_ans2',
    'l4_prod_id__que28a2_ans2',
    'l4_prod_id__que28a3_ans2',
    'l4_prod_id__que28a4_ans2',

    'l4_prod_id__que29_ans1',
    'l4_prod_id__que29_ans2'

]

###################################### DA1 & DA2 complaritions ###########################################


######################################  Quality Report ###################################################

columns_to_remove_temp = [
    'l1_status',
    'l4_status',
]  + l1list[7:] + l4list[7:]

#################################### Indi outputDownload ############################################

title = [
    'Scope',

    'Batch Name',
    'File Name',
    'ID Value',
    'ASIN',
    'Product URL',
    'Title',
    'Evidence',
    'Imagepath',
    'Question',
    'Answer-1',
    'Answer-2',
    'nile_rq',
    'Q1: is_the_context_link_valid',
    'Q2: do_you_understand_the_query',
    'Q3: what_is_the_query_type',
    'Q4: what_is_the_query_category',

    'Q5: does_the_response_contain_a_text_based_answer? Answer 1',
    'Q6: is_the_text_response_free_of_sensitive_content? Answer 1',
    'Q6A: select_the_dimension_that_was_violated_text_response? Answer 1',
    'Q6A1: select_the_sub_dimension_that_was_violated_commercially_sensitive? Answer 1',
    'Q6A2: select_the_sub_dimension_that_was_violated_offensive_content? Answer 1',
    'Q6A3: select_the_sub_dimension_that_was_violated_professional_advice? Answer 1',
    'Q6A4: select_the_sub_dimension_that_was_violated_privacy? Answer 1',
    'Q7: is_the_response_relevant_to_the_customers_query_in_the_context_of_the_conversation? Answer 1',
    'Q8: is_the_response_complete_without_any_missing_information? Answer 1',
    'Q26: does_the_response_contain_any_related_questions? Answer 1',
    'Q27: is_the_related_question_plausible? Answer 1',
    'Q28: is_the_related_question_free_of_sensitive_content? Answer 1',
    'Q28A: select_the_dimension_that_was_violated_related_question? Answer 1',
    'Q28A1: select_the_sub_dimension_that_was_violated_commercially_sensitive? Answer 1',
    'Q28A2: select_the_sub_dimension_that_was_violated_offensive_content? Answer 1',
    'Q28A3: select_the_sub_dimension_that_was_violated_professional_advice? Answer 1',
    'Q28A4: select_the_sub_dimension_that_was_violated_privacy? Answer 1',
    'Q29: General commands ? Answer 1',

    'Q5: does_the_response_contain_a_text_based_answer? Answer 2',
    'Q6: is_the_text_response_free_of_sensitive_content? Answer 2',
    'Q6A: select_the_dimension_that_was_violated_text_response? Answer 2',
    'Q6A1: select_the_sub_dimension_that_was_violated_commercially_sensitive? Answer 2',
    'Q6A2: select_the_sub_dimension_that_was_violated_offensive_content? Answer 2',
    'Q6A3: select_the_sub_dimension_that_was_violated_professional_advice? Answer 2',
    'Q6A4: select_the_sub_dimension_that_was_violated_privacy? Answer 2',
    'Q7: is_the_response_relevant_to_the_customers_query_in_the_context_of_the_conversation? Answer 2',
    'Q8: is_the_response_complete_without_any_missing_information? Answer 2',
    'Q26: does_the_response_contain_any_related_questions? Answer 2',
    'Q27: is_the_related_question_plausible? Answer 2',
    'Q28: is_the_related_question_free_of_sensitive_content? Answer 2',
    'Q28A: select_the_dimension_that_was_violated_related_question? Answer 2',
    'Q28A1: select_the_sub_dimension_that_was_violated_commercially_sensitive? Answer 2',
    'Q28A2: select_the_sub_dimension_that_was_violated_offensive_content? Answer 2',
    'Q28A3: select_the_sub_dimension_that_was_violated_professional_advice? Answer 2',
    'Q28A4: select_the_sub_dimension_that_was_violated_privacy? Answer 2',
    'Q29: General commands ? Answer 2',

    'Employee ID',
    'Employee Name',
    'Location',
    'Start Time',
    'End Time',
    'Total Time',
    'Production Date'
]

#################################### Rename Column ##############################################

ColumnName = {
    'id_value': 'ID Value',
    'baseid_id__batch_name': 'Batch Name',
    'baseid_id__filename': 'File Name',
    'question': 'Question',
    'answer_one': 'Answer 1',
    'answer_two': 'Answer 2',
    'asin': 'ASIN',
    'product_url': 'Product URL',
    'title': 'Title',
    'evidence': 'Evidence',
    'imagepath': 'Imagepath',
    'nile_rq' : 'nile_rq',
    'l1_prod_id__que1': 'DA1-Q1: is_the_context_link_valid',
    'l1_prod_id__que2': 'DA1-Q2: do_you_understand_the_query',
    'l1_prod_id__que3': 'DA1-Q3: what_is_the_query_type',
    'l1_prod_id__que4': 'DA1-Q4: what_is_the_query_category',

    'l1_prod_id__que5_ans1': 'DA1-Q5: does_the_response_contain_a_text_based_answer? Answer 1',
    'l1_prod_id__que6_ans1': 'DA1-Q6: is_the_text_response_free_of_sensitive_content? Answer 1',
    'l1_prod_id__que6a_ans1': 'DA1-Q6A: select_the_dimension_that_was_violated_text_response? Answer 1',
    'l1_prod_id__que6a1_ans1': 'DA1-Q6A1: select_the_sub_dimension_that_was_violated_commercially_sensitive? Answer 1',
    'l1_prod_id__que6a2_ans1': 'DA1-Q6A2: select_the_sub_dimension_that_was_violated_offensive_content? Answer 1',
    'l1_prod_id__que6a3_ans1': 'DA1-Q6A3: select_the_sub_dimension_that_was_violated_professional_advice? Answer 1',
    'l1_prod_id__que6a4_ans1': 'DA1-Q6A4: select_the_sub_dimension_that_was_violated_privacy? Answer 1',
    'l1_prod_id__que7_ans1': 'DA1-Q7: is_the_response_relevant_to_the_customers_query_in_the_context_of_the_conversation? Answer 1',
    'l1_prod_id__que8_ans1': 'DA1-Q8: is_the_response_complete_without_any_missing_information? Answer 1',
    'l1_prod_id__que26_ans1': 'DA1-Q26: does_the_response_contain_any_related_questions? Answer 1',
    'l1_prod_id__que27_ans1': 'DA1-Q27: is_the_related_question_plausible? Answer 1',
    'l1_prod_id__que28_ans1': 'DA1-Q28: is_the_related_question_free_of_sensitive_content? Answer 1',
    'l1_prod_id__que28a_ans1': 'DA1-Q28A: select_the_dimension_that_was_violated_related_question? Answer 1',
    'l1_prod_id__que28a1_ans1': 'DA1-Q28A1: select_the_sub_dimension_that_was_violated_commercially_sensitive? Answer 1',
    'l1_prod_id__que28a2_ans1': 'DA1-Q28A2: select_the_sub_dimension_that_was_violated_offensive_content? Answer 1',
    'l1_prod_id__que28a3_ans1': 'DA1-Q28A3: select_the_sub_dimension_that_was_violated_professional_advice? Answer 1',
    'l1_prod_id__que28a4_ans1': 'DA1-Q28A4: select_the_sub_dimension_that_was_violated_privacy? Answer 1',

    'l1_prod_id__que5_ans2': 'DA1-Q5: does_the_response_contain_a_text_based_answer? Answer 2',
    'l1_prod_id__que6_ans2': 'DA1-Q6: is_the_text_response_free_of_sensitive_content? Answer 2',
    'l1_prod_id__que6a_ans2': 'DA1-Q6A: select_the_dimension_that_was_violated_text_response? Answer 2',
    'l1_prod_id__que6a1_ans2': 'DA1-Q6A1: select_the_sub_dimension_that_was_violated_commercially_sensitive? Answer 2',
    'l1_prod_id__que6a2_ans2': 'DA1-Q6A2: select_the_sub_dimension_that_was_violated_offensive_content? Answer 2',
    'l1_prod_id__que6a3_ans2': 'DA1-Q6A3: select_the_sub_dimension_that_was_violated_professional_advice? Answer 2',
    'l1_prod_id__que6a4_ans2': 'DA1-Q6A4: select_the_sub_dimension_that_was_violated_privacy? Answer 2',
    'l1_prod_id__que7_ans2': 'DA1-Q7: is_the_response_relevant_to_the_customers_query_in_the_context_of_the_conversation? Answer 2',
    'l1_prod_id__que8_ans2': 'DA1-Q8: is_the_response_complete_without_any_missing_information? Answer 2',
    'l1_prod_id__que26_ans2': 'DA1-Q26: does_the_response_contain_any_related_questions? Answer 2',
    'l1_prod_id__que27_ans2': 'DA1-Q27: is_the_related_question_plausible? Answer 2',
    'l1_prod_id__que28_ans2': 'DA1-Q28: is_the_related_question_free_of_sensitive_content? Answer 2',
    'l1_prod_id__que28a_ans2': 'DA1-Q28A: select_the_dimension_that_was_violated_related_question? Answer 2',
    'l1_prod_id__que28a1_ans2': 'DA1-Q28A1: select_the_sub_dimension_that_was_violated_commercially_sensitive? Answer 2',
    'l1_prod_id__que28a2_ans2': 'DA1-Q28A2: select_the_sub_dimension_that_was_violated_offensive_content? Answer 2',
    'l1_prod_id__que28a3_ans2': 'DA1-Q28A3: select_the_sub_dimension_that_was_violated_professional_advice? Answer 2',
    'l1_prod_id__que28a4_ans2': 'DA1-Q28A4: select_the_sub_dimension_that_was_violated_privacy? Answer 2',

    'l1_prod_id__que29_ans1': 'DA1-Q9: General command? Answer 1',
    'l1_prod_id__que29_ans2': 'DA1-Q9: General command? Answer 2',

    'l1_emp_id__employeeID': 'DA1-EmployeeID',
    'l1_emp_id__employeeName': 'DA1-Employee Name',
    'l1_emp_id__location': 'DA1-Location',
    'l1_prod_id__start_time': 'DA1-Start Time',
    'l1_prod_id__end_time': 'DA1-End Time',
    'l1_prod_id__end_time__date': 'DA1-Production Date',

    'l4_prod_id__que1': 'QA-Q1: is_the_context_link_valid',
    'l4_prod_id__que2': 'QA-Q2: do_you_understand_the_query',
    'l4_prod_id__que3': 'QA-Q3: what_is_the_query_type',
    'l4_prod_id__que4': 'QA-Q4: what_is_the_query_category',
    
    'l4_prod_id__que5_ans1': 'QA-Q5: does_the_response_contain_a_text_based_answer? Answer 1',
    'l4_prod_id__que6_ans1': 'QA-Q6: is_the_text_response_free_of_sensitive_content? Answer 1',
    'l4_prod_id__que6a_ans1': 'QA-Q6A: select_the_dimension_that_was_violated_text_response? Answer 1',
    'l4_prod_id__que6a1_ans1': 'QA-Q6A1: select_the_sub_dimension_that_was_violated_commercially_sensitive? Answer 1',
    'l4_prod_id__que6a2_ans1': 'QA-Q6A2: select_the_sub_dimension_that_was_violated_offensive_content? Answer 1',
    'l4_prod_id__que6a3_ans1': 'QA-Q6A3: select_the_sub_dimension_that_was_violated_professional_advice? Answer 1',
    'l4_prod_id__que6a4_ans1': 'QA-Q6A4: select_the_sub_dimension_that_was_violated_privacy? Answer 1',
    'l4_prod_id__que7_ans1': 'QA-Q7: is_the_response_relevant_to_the_customers_query_in_the_context_of_the_conversation? Answer 1',
    'l4_prod_id__que8_ans1': 'QA-Q8: is_the_response_complete_without_any_missing_information? Answer 1',
    'l4_prod_id__que26_ans1': 'QA-Q26: does_the_response_contain_any_related_questions? Answer 1',
    'l4_prod_id__que27_ans1': 'QA-Q27: is_the_related_question_plausible? Answer 1',
    'l4_prod_id__que28_ans1': 'QA-Q28: is_the_related_question_free_of_sensitive_content? Answer 1',
    'l4_prod_id__que28a_ans1': 'QA-Q28A: select_the_dimension_that_was_violated_related_question? Answer 1',
    'l4_prod_id__que28a1_ans1': 'QA-Q28A1: select_the_sub_dimension_that_was_violated_commercially_sensitive? Answer 1',
    'l4_prod_id__que28a2_ans1': 'QA-Q28A2: select_the_sub_dimension_that_was_violated_offensive_content? Answer 1',
    'l4_prod_id__que28a3_ans1': 'QA-Q28A3: select_the_sub_dimension_that_was_violated_professional_advice? Answer 1',
    'l4_prod_id__que28a4_ans1': 'QA-Q28A4: select_the_sub_dimension_that_was_violated_privacy? Answer 1',

    'l4_prod_id__que5_ans2': 'QA-Q5: does_the_response_contain_a_text_based_answer? Answer 2',
    'l4_prod_id__que6_ans2': 'QA-Q6: is_the_text_response_free_of_sensitive_content? Answer 2',
    'l4_prod_id__que6a_ans2': 'QA-Q6A: select_the_dimension_that_was_violated_text_response? Answer 2',
    'l4_prod_id__que6a1_ans2': 'QA-Q6A1: select_the_sub_dimension_that_was_violated_commercially_sensitive? Answer 2',
    'l4_prod_id__que6a2_ans2': 'QA-Q6A2: select_the_sub_dimension_that_was_violated_offensive_content? Answer 2',
    'l4_prod_id__que6a3_ans2': 'QA-Q6A3: select_the_sub_dimension_that_was_violated_professional_advice? Answer 2',
    'l4_prod_id__que6a4_ans2': 'QA-Q6A4: select_the_sub_dimension_that_was_violated_privacy? Answer 2',
    'l4_prod_id__que7_ans2': 'QA-Q7: is_the_response_relevant_to_the_customers_query_in_the_context_of_the_conversation? Answer 2',
    'l4_prod_id__que8_ans2': 'QA-Q8: is_the_response_complete_without_any_missing_information? Answer 2',
    'l4_prod_id__que26_ans2': 'QA-Q26: does_the_response_contain_any_related_questions? Answer 2',
    'l4_prod_id__que27_ans2': 'QA-Q27: is_the_related_question_plausible? Answer 2',
    'l4_prod_id__que28_ans2': 'QA-Q28: is_the_related_question_free_of_sensitive_content? Answer 2',
    'l4_prod_id__que28a_ans2': 'QA-Q28A: select_the_dimension_that_was_violated_related_question? Answer 2',
    'l4_prod_id__que28a1_ans2': 'QA-Q28A1: select_the_sub_dimension_that_was_violated_commercially_sensitive? Answer 2',
    'l4_prod_id__que28a2_ans2': 'QA-Q28A2: select_the_sub_dimension_that_was_violated_offensive_content? Answer 2',
    'l4_prod_id__que28a3_ans2': 'QA-Q28A3: select_the_sub_dimension_that_was_violated_professional_advice? Answer 2',
    'l4_prod_id__que28a4_ans2': 'QA-Q28A4: select_the_sub_dimension_that_was_violated_privacy? Answer 2',

    'l4_prod_id__que29_ans1': 'QA-Q9: General commands? Answer 1',
    'l4_prod_id__que29_ans2': 'QA-Q9: General commands? Answer 2',

    'l4_emp_id__employeeID': 'QA-EmployeeID',
    'l4_emp_id__employeeName': 'QA-Employee Name',
    'l4_emp_id__location': 'QA-Location',
    'l4_prod_id__start_time': 'QA-Start Time',
    'l4_prod_id__end_time': 'QA-End Time',
    'l4_prod_id__end_time__date': 'QA-Production Date'
}

order = ['ID Value',
         'Batch Name',
         'File Name',
         'Question',
         'ASIN',
         'Product URL',
         'Title',
         'Evidence',
         'Imagepath',
         'Answer 1',
         'Answer 2',
         'nile_rq',
         'DA1-Q1: is_the_context_link_valid',
         'DA1-Q2: do_you_understand_the_query',
         'DA1-Q3: what_is_the_query_type',
         'DA1-Q4: what_is_the_query_category',

         'DA1-Q5: does_the_response_contain_a_text_based_answer? Answer 1',
         'DA1-Q6: is_the_text_response_free_of_sensitive_content? Answer 1',
         'DA1-Q6A: select_the_dimension_that_was_violated_text_response? Answer 1',
         'DA1-Q6A1: select_the_sub_dimension_that_was_violated_commercially_sensitive? Answer 1',
         'DA1-Q6A2: select_the_sub_dimension_that_was_violated_offensive_content? Answer 1',
         'DA1-Q6A3: select_the_sub_dimension_that_was_violated_professional_advice? Answer 1',
         'DA1-Q6A4: select_the_sub_dimension_that_was_violated_privacy? Answer 1',
         'DA1-Q7: is_the_response_relevant_to_the_customers_query_in_the_context_of_the_conversation? Answer 1',
         'DA1-Q8: is_the_response_complete_without_any_missing_information? Answer 1',
         'DA1-Q26: does_the_response_contain_any_related_questions? Answer 1',
         'DA1-Q27: is_the_related_question_plausible? Answer 1',
         'DA1-Q28: is_the_related_question_free_of_sensitive_content? Answer 1',
         'DA1-Q28A: select_the_dimension_that_was_violated_related_question? Answer 1',
         'DA1-Q28A1: select_the_sub_dimension_that_was_violated_commercially_sensitive? Answer 1',
         'DA1-Q28A2: select_the_sub_dimension_that_was_violated_offensive_content? Answer 1',
         'DA1-Q28A3: select_the_sub_dimension_that_was_violated_professional_advice? Answer 1',
         'DA1-Q28A4: select_the_sub_dimension_that_was_violated_privacy? Answer 1',
         'DA1-Q29: General commands? Answer 1',

         'DA1-Q5: does_the_response_contain_a_text_based_answer? Answer 2',
         'DA1-Q6: is_the_text_response_free_of_sensitive_content? Answer 2',
         'DA1-Q6A: select_the_dimension_that_was_violated_text_response? Answer 2',
         'DA1-Q6A1: select_the_sub_dimension_that_was_violated_commercially_sensitive? Answer 2',
         'DA1-Q6A2: select_the_sub_dimension_that_was_violated_offensive_content? Answer 2',
         'DA1-Q6A3: select_the_sub_dimension_that_was_violated_professional_advice? Answer 2',
         'DA1-Q6A4: select_the_sub_dimension_that_was_violated_privacy? Answer 2',
         'DA1-Q7: is_the_response_relevant_to_the_customers_query_in_the_context_of_the_conversation? Answer 2',
         'DA1-Q8: is_the_response_complete_without_any_missing_information? Answer 2',
         'DA1-Q26: does_the_response_contain_any_related_questions? Answer 2',
         'DA1-Q27: is_the_related_question_plausible? Answer 2',
         'DA1-Q28: is_the_related_question_free_of_sensitive_content? Answer 2',
         'DA1-Q28A: select_the_dimension_that_was_violated_related_question? Answer 2',
         'DA1-Q28A1: select_the_sub_dimension_that_was_violated_commercially_sensitive? Answer 2',
         'DA1-Q28A2: select_the_sub_dimension_that_was_violated_offensive_content? Answer 2',
         'DA1-Q28A3: select_the_sub_dimension_that_was_violated_professional_advice? Answer 2',
         'DA1-Q28A4: select_the_sub_dimension_that_was_violated_privacy? Answer 2',
         'DA1-Q29: General commands? Answer 2',

         'DA1-EmployeeID',
         'DA1-Employee Name',
         'DA1-Location',
         'DA1-Start Time',
         'DA1-End Time',
         'DA1-Production Date',

         'QA-Q1: is_the_context_link_valid',
         'QA-Q2: do_you_understand_the_query',
         'QA-Q3: what_is_the_query_type',
         'QA-Q4: what_is_the_query_category',

         'QA-Q5: does_the_response_contain_a_text_based_answer? Answer 1',
         'QA-Q6: is_the_text_response_free_of_sensitive_content? Answer 1',
         'QA-Q6A: select_the_dimension_that_was_violated_text_response? Answer 1',
         'QA-Q6A1: select_the_sub_dimension_that_was_violated_commercially_sensitive? Answer 1',
         'QA-Q6A2: select_the_sub_dimension_that_was_violated_offensive_content? Answer 1',
         'QA-Q6A3: select_the_sub_dimension_that_was_violated_professional_advice? Answer 1',
         'QA-Q6A4: select_the_sub_dimension_that_was_violated_privacy? Answer 1',
         'QA-Q7: is_the_response_relevant_to_the_customers_query_in_the_context_of_the_conversation? Answer 1',
         'QA-Q8: is_the_response_complete_without_any_missing_information? Answer 1',
         'QA-Q26: does_the_response_contain_any_related_questions? Answer 1',
         'QA-Q27: is_the_related_question_plausible? Answer 1',
         'QA-Q28: is_the_related_question_free_of_sensitive_content? Answer 1',
         'QA-Q28A: select_the_dimension_that_was_violated_related_question? Answer 1',
         'QA-Q28A1: select_the_sub_dimension_that_was_violated_commercially_sensitive? Answer 1',
         'QA-Q28A2: select_the_sub_dimension_that_was_violated_offensive_content? Answer 1',
         'QA-Q28A3: select_the_sub_dimension_that_was_violated_professional_advice? Answer 1',
         'QA-Q28A4: select_the_sub_dimension_that_was_violated_privacy? Answer 1',
         'QA-Q29: General commands? Answer 1',

         'QA-Q5: does_the_response_contain_a_text_based_answer? Answer 2',
         'QA-Q6: is_the_text_response_free_of_sensitive_content? Answer 2',
         'QA-Q6A: select_the_dimension_that_was_violated_text_response? Answer 2',
         'QA-Q6A1: select_the_sub_dimension_that_was_violated_commercially_sensitive? Answer 2',
         'QA-Q6A2: select_the_sub_dimension_that_was_violated_offensive_content? Answer 2',
         'QA-Q6A3: select_the_sub_dimension_that_was_violated_professional_advice? Answer 2',
         'QA-Q6A4: select_the_sub_dimension_that_was_violated_privacy? Answer 2',
         'QA-Q7: is_the_response_relevant_to_the_customers_query_in_the_context_of_the_conversation? Answer 2',
         'QA-Q8: is_the_response_complete_without_any_missing_information? Answer 2',
         'QA-Q26: does_the_response_contain_any_related_questions? Answer 2',
         'QA-Q27: is_the_related_question_plausible? Answer 2',
         'QA-Q28: is_the_related_question_free_of_sensitive_content? Answer 2',
         'QA-Q28A: select_the_dimension_that_was_violated_related_question? Answer 2',
         'QA-Q28A1: select_the_sub_dimension_that_was_violated_commercially_sensitive? Answer 2',
         'QA-Q28A2: select_the_sub_dimension_that_was_violated_offensive_content? Answer 2',
         'QA-Q28A3: select_the_sub_dimension_that_was_violated_professional_advice? Answer 2',
         'QA-Q28A4: select_the_sub_dimension_that_was_violated_privacy? Answer 2',
         'QA-Q29: General commands? Answer 2',

         'QA-EmployeeID',
         'QA-Employee Name',
         'QA-Location',
         'QA-Start Time',
         'QA-End Time',
         'QA-Production Date'
         ]


without = ['DA1-EmployeeID',
           'DA1-Employee Name',
           'DA1-Location',
           'DA1-Start Time',
           'DA1-End Time',
           'DA1-Total Time Taken',
           'DA1-Production Date',


           'QA-EmployeeID',
           'QA-Employee Name',
           'QA-Location',
           'QA-Start Time',
           'QA-End Time',
           'QA-Total Time Taken',
           'QA-Production Date'
           ]

###################################### Hourly Tracking ##########################

rnmhourlycolumn = {'empname': 'Employee Name', 'empid': 'Employee ID', 'targetempid__location': 'Location',
                   'target': 'Target', 'filename': 'File Name',
                   '1.0': '01-02',
                   '2.0': '02-03',
                   '3.0': '03-04',
                   '4.0': '04-05',
                   '5.0': '05-06',
                   '6.0': '06-07',
                   '7.0': '07-08',
                   '8.0': '08-09',
                   '9.0': '09-10',
                   '10.0': '10-11',
                   '11.0': '11-12',
                   '12.0': '12-13',
                   '13.0': '13-14',
                   '14.0': '14-15',
                   '15.0': '15-16',
                   '16.0': '16-17',
                   '17.0': '17-18',
                   '18.0': '18-19',
                   '19.0': '19-20',
                   '20.0': '20-21',
                   '21.0': '21-22',
                   '22.0': '22-23',
                   '23.0': '23-00',
                   '00.0': '00-01'}

####################################### UT Report #################################################

utcolumns = {
    'date': 'Date',
    'empid': 'Employee ID',
    'empname': 'Employee Name',
    'filename': 'Filename',
    'location': 'Location',
    'language': 'Language',
    'productiontime': 'Production Time'
}
