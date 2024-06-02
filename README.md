# Final Project 

## **Joker Game for 4 players****

=> დავამატო 2 გუნდად (ორი-ორზე) თამაშის ვერსიაც - რომელსაც თავდაპირველად აირჩევს მოთამაშეები

## **შეფასების სქემა**

1. კოდის გითჰაბზე განთავზება ახალ რეპოზიტორიაში
2. პროექტის ფაილების სტრუქტურის გამართულობა
3. Readme.md ფაილის არსებობა და მინიმალური ინფორმაციის განთავსება პროექტზე
4. კოდის სტრუქტურა უნდა იყოს გამართული
5. სუფთა კოდი(Clean code - პრაქტიკების გამოყენება)
6. სწორად უნდა იყოს შერჩეული სახელები:

         1.ცვლადებისთვის 
         2.ფუნქციებისთვის 
         3.კლასებისთვის

7. კოდი უნდა იყოს ადვილად წაკითხვადი
8. ფაილების სახელები უნდა იყოს შერჩეული სტანდარტების დაცვით
9. ფაილების სახელები უნდა იყოს ინფორმატიული
10. დასმული პრობლემა სწორად არის გადაჭრილი
11. სალექციო კურსის განმავლობაში შესწავლილი საკითხების გამოყენება

        1.ციკლები
        2.If-else ს გამოყენება
        3.მონაცემთა სტრუქტურები (List, dict, tuple, string, set)
        4.ფუნქციების გამოყენება
        5.ფაილებთან მუშაობა
        6.კლასების გამოყენება
        7.გამონაკლისების დამუშავება (Exception, try-except)
        8.მოდულების გამოყენება


## **თამაშის წესები** 

ჯოკერი 4 მოთამაშისთვის

პროგრამამ უნდა მისცეს მომხმარებელს საშუალება რომ შეიყვანოს
მოთამაშეების სახელები. თამაშში გვყავს 4 მოთამაშე. 

თამაშში გვაქვს შემდეგი ცნებები:

* **გათამაშება** - გათამაშება ნიშნავს კარტის ერთ დარიგებას და სრულად ამოწურვას
* **კარტის დამრიგებელი** - მოთამაშე რომელიც მიმდინარე ხელზე არიგებს კარტს.
* **ოთხეული** - 4 გათამაშება გვაძლევს ოთხეულს 
* **სიტყვა** - ყოველი მოთამაშე თითოეული გათამაშების დროს ამბობს რამდენი კარტის წაყვანას შეძლებს. ამას ვუწოდებთ სიტყვას. 
* **სიტყვის შესრულება** - ნიშნავს რომ თუ მოთამაშემ თქვა რომ აიყვანდა x კარტს და ნამდვილად აიყვანა x კარტი. არც მეტი არც ნაკლები 
* **ჯარიმა** - თუ მოთამაშემ თქვა არანულოვანი სიტყვა, და ვერ შეძლო კარტის წაყვანა, ის ჯარიმდება 500 ქულთ. 
* **ქულა** - თითოეულ სიტყვას შეესაბამება ქულა, თამაშის ბოლოს ჯამდება ქულები და ყველაზე მეტი ქულის მქონე მოთამაშე იმარჯვებს 
* **პრემია** - ოთხეულის ბოლოს, თუ მოთამაშემ ყველა სიტყვა შეასრულა, მას ეძლევა პრემია. პრემია გულისხმობს რომ, მას დაემატება უმაღლესი ქულა ოთხეულიდან.
**კოზირი** - კოზირის არჩევა ხდება გათამაშების პირველი მოთამაშის მიერ, მას შეუძლია აირჩიოს ნებისმიერი ფერი. შესაძლოა მოთამაშემ არ აირჩიოს არცერთი ფერი, ასეთ გათამაშებას ეწოდება უკოზირო გათამაშება. 
* **კარტის გაჭრა** - გაჭრა ნიშნავს კარტის დამარცხებას, ვიტყვით რომ A ჭრის B-ს, როცა A-ს აქვს უფრო მაღალი მნიშვნელობა ვიდრე B-ს. კარტები ეკუთვნის გამჭრელი კარტის მეპატრონე მოთამაშეს


Მოთამაშეების სახელების შეყვანის მერე შემთხვევითობის პრინციპით უნდა აირჩეს ბოლო მოთამაშე. 

რომ აირჩევა ბოლო მოთამაშე, პროგრამამ ყველა მოთამაშეს უნდა დაურიგოს 9-9 კარტი 36 კარტიანი დასტიდან. 

1. ვთქვათ გვყავს მოთამაშეები შემდეგი სახელებით: A, B, C და D.
2. ვთქვათ, ბოლო მოთამაშეა D. პირველი, მეორე და მესამე მოთამაშეები შეგვიძლია ნებისმიერად ავირჩიოთ.
3. დავუშვათ ავირჩიეთ შემდეგნაირად: პირველი - A მეორე - B მესამე - C მეოთხე - D ეს მიმდევრობა არის მნიშვნელოვანი, რადგანაც ამ მიმდევრობის მიხედვით მიმდინარეობს თამაში. 
4. თამაშის დასაწყისში კარტის დამრიგებელი არის ბოლო მოთამაშე, ჩვენს შემთხვევაში ეს იქნება მოთამაშე სახელით - D. 
5. შემდეგი კარტის დამრიგებელი აირჩევა რიგის მიხედვით და იქნება A, შემდეგი იქნება B, შემდეგი C, შემდეგი ისევ D და ასე შემდეგ თამაშის დასრულებამდე.
6. მას შემდეგ რაც მოთამაშეებს დაურიგდებათ 9-9 კარტი, პირველ მოთამაშეს გათამაშებაში უნდა გაეხსნას მხოლოდ პირველი 3 კარტი, რათა მან შეძლოს კოზირის არჩევა. 
7. კოზირის არჩევის შემდეგ, მას უნდა გაეხსნას ყველა კარტი და პროგრამამ უნდა მოსთხოვოს სიტყვის თქმა. სიტყვა არ უნდა იყოს 0-ზე ნაკლები და 9 ზე მეტი. 
8. მას შემდეგ რაც პირველი მოთამაშე იტყვის სიტყვას, მეორე მოთამაშეს უნდა გაეხსნას კარტები და პროგრამამ უნდა მოსთხოვოს მას სიტყვის თქმა. ასე უნდა გაგრძელდეს ბოლო მოთამაშემდე. 
9. გახსოვდეთ, რომ ბოლო მოთამაშე არის კარტის დამრიგებელი. ბოლო მოთამაშესაც უნდა გაეხსნას თავისი კარტები და პროგრამამ უნდა მოსთხოვოს სიტყვის შეყვანა, თუმცა აქ ემატება დამატებითი შეზღუდვა:ბოლო მოთამაშეს არ აქვს ისეთი სიტყვის თქმის უფლება, რომ სიტყვების ჯამმა შეადგინოს 9. მაგალითად, თუ სიტყვები ასეთია A -> 2, B -> 3, C -> 2, მოთამაშე D-ს არ აქვს 2 ის თქმის უფლება. უნდა თქვას 2-ზე ნაკლები ან მეტი სიტყვა. 
10. მას შემდეგ რაც ყველა მოთამაშე იტყვის სიტყვას, იწყება თამაში. 
11. თამაშს იწყებს პირველი მოთამაშე. მას შეუძლია ჩამოვიდეს ნებისმიერი კარტი.
12. ყოველი შემდეგი მოთამაშე ვალდებულია, რომ ჩამოვიდეს პირველად ჩამოსული კარტის ფერის კარტი (ასეთის არსებობის შემთხვევაში) ან  ჩამოვიდეს კოზირი (თუ გათამაშება არ არის უკოზირო) ან ჯოკერი. პროგრამამ უნდა უზრუნველყოს ამ წესების დაცვა და არ მისცეს მოთამაშეებს მათი დარღვევის უფლება.
13. მას შემდეგ რაც ყველა მოთამაშე ჩამოვა კარტს, უნდა დადგინდეს უმაღლესი კარტის ავტორი და 4 კარტი გადაეცემა მას. 
14. როგორ უნდა დადგინდეს კარტის მაღლობა იხილეთ ქვემოთ.
15. შემდეგი კარტის ჩამოსვლის უფლება აქვს, წინა ჩამოსვლის გამარჯვებულს (ვისაც 4 კარტი გადაეცა). ასე გრძელდება სანამ მოთამაშეები არ ამოწურავენ კარტებს.
16. როცა გათამაშებაში კარტები ამოიწურება, პროგრამამ უნდა დაითვალოს ვინ რამდენი კარტი წაიღო, ერთ ჩამოსვლაზე წაღებული 4 კარტი ითვლება ერთად.
17. თუ მოთამაშემ სიტყვა შეასრულა ეწერება სრული ქულა, თუ ვერ შეასრულა(გადააჭარბა ან ნაკლები კარტი აიღო) ეწერება ამორტიზებული ქულა. იხილეთ ცხრილი სრული და ამორტიზებული ქულებისთვის:

![Screenshot 2024-06-02 125319.png](..%2FOneDrive%2FDesktop%2FScreenshot%202024-06-02%20125319.png)

* ქულების ცხრილში შეცდომა. როცა სიტყვა არის არანულოვანი, და აყვანილი კარტების რაოდენობა ნულია. მოთამაშე ჯარიმდება. პირველ სვეტში სულ ხიშტები უნდა იყოს პირველი სტრიქონის გარდა


18. ასე უნდა ჩატარდეს 4 გათამაშება. 
19. 4 გათამაშების მერე სრულდება ოთხეული. 
20. ოთხეულის დასასრულს უნდა დადგინდეს რომელმა მოთამაშემ დაიმსახურა პრემია. 
21. იმ მოთამაშეებს, რომლებმაც დაიმსახურეს პრემია, ოთხეულიდან ემატებათ ყველაზე მაღალი ქულა.


      მაგალითად, თუ მოთამაშე A-ს ჰქონდა შემდეგი ქულები, 100, 200, 100, 250, მისი ოთხეულის ჯამური ქულა იქნება 900.
      პროგრამამ მოთამაშეებს უნდა ათამაშოს 4 ოთხეული და გამოავლინოს გამარჯვებული. 

    
24. პროგრამამ ყოველ ახალი გათამაშების დაწყების წინ უნდა დახატოს მოთამაშეების ცხრილი, რომელშიც მოცემული იქნება მოთამაშეების სახელები მიმდევრობით, მათი სიტყვები და ქულები. 
25. როგორ ხდება კარტის სიმაღლის დადგენა? 
26. სანამ ამ შეკითხვას ვუპასუხებთ მანამდე უნდა ვთქვათ რა კარტებისგან შედგება ჩვენი დასტა. დასტაში ჩვენ გვაქვს 36 კარტი. 

        4 ფერის კარტი შემდეგი მნიშვნელობებით A, K, Q, J, 10, 9, 8, 7, 6 და კიდევ 2 Joker. ეს ჯამში 38 გამოდის,
        ამიტომ მას ვაკლებთ 6-იან ჯვარსა და 6-იან ყვავს.

        ერთი ფერის კარტებში, ყველაზე მაღალია მაღალი მნიშვნელობის კარტი.

27. მაგალითად A უფრო მაღალია ვიდრე 9, 8 უფრო მაღალია ვიდრე 6 და ა შ. 
28. შენი კარტი ითვლება უფრო მაღალ კარტად, თუ მოთამაშეს უჭრი კარტს თავისი ფერის კარტით. თუ შენი კარტის ფერი განსხვავებულია, მაშინ ვერ გაუჭრი კარტს, მიუხედავად იმისა რომ მასზე მაღალი მნიშნველობა შეიძლება გქონდეს. მაგალითად 8-იან გულს, ვერ გაჭრის K ჯვარი. 
29. კოზირს შეუძლია ნებისმიერი კარტის გაჭრა, ფერს არ აქვს მნიშვნელობა. კოზირზე მაღალი მხოლოდ სხვა კოზირია, რომელსაც აქვს უფრო მაღალი მნიშვნელობა. 
30. Joker არის ყველაზე მაღალი კარტი თამაშში და შეუძლია ნებისმიერი კარტის გაჭრა, მათ შორის ჯოკრის გაჭრაც. უგულებელყავით ის ფაქტი რომ მოთამაშეებს შეუძლიათ ერთმანეთის კარტების დანახვა.



# **Structure of the Final Project:**


### **Classes:**

(კლასები და მეთოდები ბოლოსკენ შევქმნა, როცა მზად მექნება ძირითადი ფუნქციები რომ მეთოდებად გარდავქმნა)
1. 

### **Functions:** 
1. კონსტანტების განსაზღვრა:

        მოთამაშეების რაოდენობა
        კარტის მნიშვნელობები
        სიტყვისა და აყვანილი კარტების მიხედვით ქულის გამოთვლა (თავდაპირველად Dict შევქმნა, მერე ფუნქციად გადავაკეთებ)


2. მოთამაშეების სახელების მიღება; (იმ შემთხვევის გათვალისწინება, რომ 4 უნდა იყოს (არც მეტი არც ნაკლები რომ თამაში დაიწყოს))
3. თამაშის წესის არჩევა - 4-ივე დამოუკიდებელი მოთამაშის სახით თუ ორი-ორზე:
   <p> * თუ ორი-ორზე, რომელი მოთამაშეები იქნება ერთად (არჩევა და თამაშის დასაწყებად მომზადება)
3. ბოლო მოთამაშის შემთხვევითობით არჩევა და მოთამაშეების რიგითობის განსაზღვრა. მოთამაშეების რიგითობის მიხედვით დაბეჭდვა
4. 36 კარტიანი დასტის გენერირება და აჩეხვა
5. გათამაშება - ბოლო მოთამაშის მიერ კარტის დარიგება (9-იანები ანუ ყველა კარტი რიგდება) - 3-3 კარტის დარიგების შემდეგ პირველ მოთამაშეს ვაჩვენებთ სამ კარტს კოზირის არჩევისთვის - შემდეგ სრულად ვარიგებთ.
6. კარტის დამრიგებელი თავდაპირველად არის ბოლო მოთამაშე, შემდეგ რიგითობის მიხედვით. 
7. პირველი მოთამაშისთვის პირველი 3 კარტის გახსნა
8. პირველი მოთამაშის მიერ კოზირის არჩევა: 4 კოზირის ან უკოზიროს არჩევის ვერსიები აქვს
9. ყველა კარტის დარიგების შემდეგ, პირველ მოთამაშემ უნდა შეიყვანოს თავისი სიტყვა (0-9) შორის. 
10. მეორე მოთამაშემ შეიყვანოს სიტყვა
11. მესამე მოთამაშემ შეიყვანოს სიტყვა
12. მეოთხე მოთამაშემ შეიყვანოს სიტყვა (თუმცა შევსების შემთხვევა გავითვალისწინოთ, რამდენს ვერ იტყვის)
13. ყველა როცა იტყვის სიტყვას დაიბეჭდოს ვინ რამდენი თქვა და დაიწყოს პირველი ხელის თამაში:
  
        პირველი მოთამაშე ჩამოდის პირველ კარტს
        სხვა მოთამაშეებმა უნდა (რომ არ დაარღვიოს წესი ეს შემთხვევაც დავაზღვიო) ჩამოვიდეს იმავე ფერის კარტი ან კოზირი
        თუ კოზირი არ ჰყავს ან უკოზირო თამაშია სხვა ფერის კარტი ან ჯოკერი

14. ჩამოსულ 4 კარტს შორის ვისაც მაღალი ჰყავს იმას გადაეცეს 4-ვე კარტი - ქულების მეტობის ცალკე ფუნქციის შემქნა (აღებულ ქულებს დაემატოს 1 პარალელურად)
15. ვინც წაიღებს 4 კარტს იმან ჩამოვიდეს მისთვის სასურველი კარტი - შემდეგ მე-13 წესის მიხედვით დანარჩენმა მოთამაშეებმა. 
16. როცა მოთამაშეები კარტს ჩამოდიან (ეს კარტები ამოვიღოთ მათ ხელში არსებული კარტებიდან)
17. ასე გაგრძელდეს 9-ვე კარტის ჩამოსვლამდე. ყველა კარტს რომ ჩამოვლენ და ბოლო 4 კარტიც წავა რომელიმე მოთამაშესთან, ეკრანზე დაიბეჭდოს პირველი ხელის შედეგები: ვინ რამდენი თქვა და რამდენი აიყვანა.
18. დაიწყოს მეორე ხელისთვის კარტების აჩეხვა, დარიგება და კოზირის არჩევა და თამაში მე-4 პუნქტიდან მე-17-ეს ჩათვლით პრინციპით. 
19. სულ გათამაშდეს 4 ხელი. 
20. 4 ხელის დასრულების შემდეგ ქულების დაბეჭდვა ეკრანზე. 
21. 4 ხელის შედეგების მიხედვით პრემიაზე გასული მოთამაშ(ეებ)ის გამოვლენა
22. პრემიაზე თუ გავიდა ვინმე: დანარჩენ მოთამაშეებს შორის ყველაზე მაღალქულიანის გამოვლენა (4-ვე ხელის შედეგებით) და ამ ქულის პრემიაზე გასულისთვის დამატება
23. ეკრანზე დაიბეჭდოს გამარჯვებული მოთამაშის სახელი. 
24. Game Over! 











