String urlConnect = "http://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json";
URL url = new URL(urlConnect);
HttpURLConnection conn = (HttpURLConnection)url.openConnection();
InputStreamReader isr = new InputStreamReader(conn.getInputStream());
BufferedReader in = new BufferedReader(isr);
String line  = in.readLine(); 