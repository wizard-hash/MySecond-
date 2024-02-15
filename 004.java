
1	/* 
2	 * Decompiled with CFR 0.0. 
3	 *  
4	 * Could not load the following classes: 
5	 *  java.lang.Object 
6	 *  java.lang.String 
7	 *  java.util.Random 
8	 *  kotlin.random.Random 
9	 *  org.jetbrains.annotations.NotNull 
10	 *  w9.t 
11	 *  z9.c 
12	 */ 
13	//package z9; 
14	 
15	import kotlin.random.Random; 
16	import org.jetbrains.annotations.NotNull; 
17	import w9.t; 
18	import z9.c; 
19	 
20	public abstract class a 
21	extends Random { 
22	    @NotNull 
23	    public abstract java.util.Random getImpl(); 
24	 
25	    public int nextBits(int n2) { 
26	        return c.takeUpperBits((int)this.getImpl().nextInt(), (int)n2); 
27	    } 
28	 
29	    public boolean nextBoolean() { 
30	        return this.getImpl().nextBoolean(); 
31	    } 
32	 
33	    @NotNull 
34	    public byte[] nextBytes(@NotNull byte[] arrby) { 
35	        t.checkNotNullParameter((Object)arrby, (String)"array"); 
36	        this.getImpl().nextBytes(arrby); 
37	        return arrby; 
38	    } 
39	 
40	    public double nextDouble() { 
41	        return this.getImpl().nextDouble(); 
42	    } 
43	 
44	    public float nextFloat() { 
45	        return this.getImpl().nextFloat(); 
46	    } 
47	 
48	    public int nextInt() { 
49	        return this.getImpl().nextInt(); 
50	    } 
51	 
52	    public int nextInt(int n2) { 
53	        return this.getImpl().nextInt(n2); 
54	    } 
55	 
56	    public long nextLong() { 
57	        return this.getImpl().nextLong(); 
58	    } 
59	} 
60	 
61	 
