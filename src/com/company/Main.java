package com.company;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.*;

public class Main {
    /**
     * 打印内容
     * @param index 索引
     * @param object 对象
     */
    public static void print(int index, Object object) {
        System.out.println(String.format("{%d}, %s", index, object.toString()));
    }
    public static void demoOperation() {
        print(1, 5 + 2);
        int a = 11;
        double b = 2.2f;
        a += 2;
        print(14,a);
    }
    public static void demoString() {
        String str = "hello world";
        print(1, str.indexOf('o')); //查看某个字符是否存在
        print(1, str.charAt(3)); //查看一个String的该索引值的值是多少
        print(3,str.codePointAt(1));//查看第2个字符的ascii码
        print(4,str.compareToIgnoreCase("HELLO WORLD"));
        print(5,str.compareTo("hello wolrd"));
        print(6,str.compareTo("hello colrd"));
        print(7,str.contains("hello"));
        print(8,str.concat("!!!!"));
        print(10,str.toUpperCase());
        print(11,str.endsWith("world"));
        print(12,str.startsWith("hello"));
        print(13,str.replace('o', 'e'));
        print(14,str.replaceAll("o|l", "e"));
        print(15,str.replaceAll("hello", "ko"));

        StringBuilder sb = new StringBuilder();
        sb.append("xc ");
        sb.append(1.2);
        sb.append("dssd");
        print(16, sb.toString());
    }
    public static void demoControlFlow() {

    }
    public static void  demoList() {
        List<String> strList = new ArrayList<String>(10);
        for (int i = 0; i < 4; ++i) {
            strList.add(String.valueOf(i));
        }
        print(1, strList);

        List<String> strlist1 = new ArrayList<>();
        strlist1.addAll(strList);
        print(2, strlist1);
        strlist1.remove(3);
        print(3, strlist1);
        strlist1.remove(String.valueOf(1));
        print(4, strlist1);
        print(5, strlist1.get(1));

        Collections.reverse(strList);
        print(6, strList);
        Collections.sort(strList);
        print(7, strList);
        Collections.sort(strList, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return o1.compareTo(o2);
            }
        });
        strList.sort(new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return o2.compareTo(o1);
            }
        });
    }

    public static void demoHashTable() {
        Map<String, String> map = new HashMap<String, String>();
        for(int i = 0; i < 4; ++i) {
            map.put(String.valueOf(i), String.valueOf(i*i));
        }
        print(1,map);
        for(Map.Entry<String, String> entry : map.entrySet()) {
            print(2, entry.getKey() + "|" + entry.getValue());
        }
        print(3, map.values());
        print(4, map.keySet());
        print(4, map.get("3"));
        print(6, map.containsKey("A0"));
        map.replace("3", "33");
        print(7, map.get("3"));
    }
    public static void demoSet() {
        Set<String> strSet = new HashSet<>();
        for (int i = 0; i < 3; ++i) {
            strSet.add(String.valueOf(i));
        }
        print(1, strSet);
        strSet.remove(String.valueOf(1));
        print(2, strSet);
        print(3,strSet.contains(String.valueOf(1)));
        print(4, strSet.isEmpty());
        print(4, strSet.size());
        strSet.addAll(Arrays.asList(new String[]{"A", "B", "C"}));
        print(6, strSet);
        for (String value : strSet) {
            print(1, value);
        }
    }
    public static void demoException() {
        try {
            int k = 2;
            k = 2 / 0;
        } catch (Exception e) {
            print(2, e.getMessage());
        } finally {
            print(3, "finally");
        }
    }
    public static void demo00() {
        Animal a = new Animal("kai", 2);
        a.say();
        Animal human = new Human("jii", 12, "China");
        human.say();
    }
    public static void demoFunction() {
        Random random = new Random();
        random.setSeed(12);
        print(1, random.nextInt(1000));
        print(2, random.nextFloat());

        List<Integer> array = Arrays.asList(new Integer[] {1, 2, 3, 4, 5});
        Collections.shuffle(array);
        print(3, array);

        Date date = new Date();
        print(4, date);
        print(5, date.getTime());

        DateFormat df = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        print(6, df.format(date));

        print(7, UUID.randomUUID());

        print(8, Math.log(10));
        print(9, Math.min(3, 10));
        print(10, Math.max(4, 120));
        print(11, Math.ceil(2.5));
        print(12, Math.floor(3.4));
    }
    public static void main(String[] args) {
        demoOperation();
        demoString();
        demoList();
        demoSet();
        demoException();
        demo00();
        demoFunction();

    }
}
