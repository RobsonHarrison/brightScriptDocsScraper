# Roku app tracing (with Perfetto)
You can use [Perfetto](https://perfetto.dev/docs/) to record, analyze, and visualize traces of your Roku apps to pinpoint where you can reduce resource consumption and optimize performance. Tracing captures and visualizes the events in your app on a timeline, which provides you with a detailed graphical view of what your app is doing over time.
The [BrightScript Language extension for VSCode](https://marketplace.visualstudio.com/items?itemName=RokuCommunity.brightscript) lets you launch your app, record and save a trace, and then view it in Perfetto directly (alternatively, you can use ECP to record a trace and view it in Perfetto). You can then explore the trace in Perfetto by using the WASD keys on your keyboard to zoom and pan, and your mouse to expand process tracks (rows) into their constituent thread tracks. You can also execute SQL-based queries in Perfetto.
![perfetto-ui-overview](https://image.roku.com/ZHZscHItMTc2/perfetto-ui.png)
> **Roku OS 15.2 adds support for BrightScript heap graphs**
> You can now capture and visualize BrightScript heap graphs to pinpoint memory issues in your app with more speed and precision.
> Perfetto displays heap snapshots as interactive flame graphs in a separate VS Code tab. The X-axis shows memory usage, while the Y-axis shows retention paths from root to each object. You can sort by size or count to identify the largest memory consumers, then drill down into object hierarchies.
> To generate heap graphs for memory profiling, you need Roku OS 15.2 (or higher), [BrightScript Language extension for VSCode](https://marketplace.visualstudio.com/items?itemName=RokuCommunity.brightscript) (2.60.1 or higher), and a Roku device in developer mode. See BrightScript heap graphs for more information.
## Prerequisites
To record a trace, developers need the following:
  * Roku OS 15.1 (or later)
  * A Roku device with [developer mode enabled](https://developer.roku.com/docs/developer-program/getting-started/developer-setup.md).
  * Roku app (you can record a trace with an app running in a [sideloaded](https://developer.roku.com/docs/developer-program/getting-started/developer-setup.md#sideloading-channels), beta, or production environment).
    * For a sideloaded app, the manifest must enable the **run_as_process** attribute (run_as_process=1).
    * For a [beta](https://developer.roku.com/docs/developer-program/publishing/channel-publishing-guide.md#beta-channel-guidelines) or [production](https://developer.roku.com/docs/developer-program/publishing/channel-publishing-guide.md#public-channel-guidelines) app, the developer must own the app (your [device must be keyed with key used to sign the app package](https://developer.roku.com/docs/developer-program/publishing/packaging-channels.md#rekeying-from-an-existing-package)). T
  * Trace recording app. You can record an app trace using [BrightScript Language extension for VSCode](https://marketplace.visualstudio.com/items?itemName=RokuCommunity.brightscript) or ECP and a websocket client.

## Using VSCode to enable and record Perfetto traces
You can enable and record a Perfetto trace with the [BrightScript Language extension for VSCode](https://marketplace.visualstudio.com/items?itemName=RokuCommunity.brightscript) following these steps:
### Enabling Perfetto
  1. Verify that you have done the following:
    1. Installed VSCode.
    2. Installed the latest version of [BrightScript Language extension for VSCode](https://marketplace.visualstudio.com/items?itemName=RokuCommunity.brightscript).
    3. Created a [**launch.json** configuration file](https://rokucommunity.github.io/vscode-brightscript-language/Debugging/index.html) in your app directory.
    4. Updated your Roku device to Roku OS 15.2 (or later)
  2. In the **launch.json** file, add the following **profiling** object to the **configurations** object:

```
   {
       "version": "0.2.0",
       "configurations": [
         {
           "type": "brightscript",
           "request": "launch",
           "name": "BrightScript Debug: Launch",
           "host": "<Roku device IP address>",
           "password": "<Roku device password>",

            //add the following to enable Perfetto tracing
           "profiling": {
               "tracing": {
                   "enable": true,
               }
             }
           }
       ]
   }

```

### Recording a Perfetto trace
To record trace data for a session in VSCode, follow these steps:
  1. In VS Code, add your app folder (select **File** > **Open Folder**).
![perfetto-ui-overview - roku600px](https://image.roku.com/ZHZscHItMTc2/vscode-open-folder.png)
  2. Select **Run >Start Debugging** (or press F5) to sideload your app. Tracing begins automatically.
  3. Test your app.
  4. When you are done testing, click the red **Stop Perfetto Tracing** button.
![perfetto-ui-overview - roku400px](https://image.roku.com/ZHZscHItMTc2/stop-perfetto.png)
  5. The recorded Perfetto trace opens in a new window. Use the WASD keys on your keyboard to zoom and pan, and use your mouse to expand process tracks (rows) into their constituent thread tracks.
![perfetto-ui-overview - roku600px](https://image.roku.com/ZHZscHItMTc2/vscode-peretto-visual.png)

### Capturing heap graphs
To capture the BrightScript heap graph, follow these steps:
  1. Start recording a trace and test your app.
  2. Click the **Capture heap snapshot** button one or more times during the recording.
![perfetto-ui-overview - roku400px](https://image.roku.com/ZHZscHItMTc2/capture-heap-snapshot.png)
  3. Click the **Stop Perfetto Tracing** button when you are done testing.
  4. The **Java heap graph** in the **Current Selection** tab displays the SceneGraph and BrightScript objects as a [flamegraph](https://www.brendangregg.com/flamegraphs.html). You can sort the objects either by allocation size or object count, ordering callstacks from left-to-right according to which have the largest size or count.
![perfetto-ui-overview - roku600px](https://image.roku.com/ZHZscHItMTc2/capture-heap-snapshot-2.png)
  5. A single Perfetto trace can hold multiple heap graphs, with each heap graph represented by a selectable **Heap Profile** event.
![perfetto-ui-overview - roku600px](https://image.roku.com/ZHZscHItMTc2/select-heap-profile.png)

> **Shortest Path used to display heap graph** The heap graph is always shown as the shortest path from a _root_ to any given object. This can sometimes lead to charts that might have unexpected structure. For example, if you have a Scene that owns a Grid which in turn owns a ContentNode, you might expect a chart reflecting this:
>
```
== MyScene ==========
  -- MyGrid ---------
    - MyContentNode -

```

> However, if there is also a reference to the content node from directly from the domain - perhaps because it is referenced by a local variable, then this path will be preferentially displayed:
>
```
== $bsProc-MyScene-Render ====   == MyScene ==
  - MyContentNode -               -- MyGrid --

```

## Using ECP to enable and record Perfetto traces
You can enable and record a Perfetto trace with ECP following these steps:
### Enabling Perfetto
To enable tracing for an app, send the enable Perfetto command with the channel ID:

```
curl -X POST "http://192.168.1.86:8060/perfetto/enable/dev"

```

The ECP response will have the following syntax:

```
<?xml version="1.0" encoding="UTF-8" ?>
<perfetto-enable>
    <enabled-channels>
        <channel>dev</channel>
    </enabled-channels>
    <timestamp>1762473265350</timestamp>
    <timestamp-end>1762473265350</timestamp-end>
    <status>OK</status>
</perfetto-enable>

```

Once enabled, tracing starts automatically each time the app is launched
> ECP does not have a corresponding disable Perfetto command. The list of enabled apps is cleared on reboot.
### Recording a Perfetto trace
To record trace data for a session, using a websocket client to connect to the device (for example, [websocat](https://github.com/vi/websocat)). The websocket emits a stream of bytes, which is the Protobuf-encoded Perfetto trace from the device.

```
websocat --binary ws://$ip:8060/perfetto-session > perfetto_data.trace

```

Data stops streaming when the client disconnects. If the client reconnects, the stream resumes.
> Roku only supports a single websocket connection at a time.
### Visualizing ECP-generated trace files in Perfetto
You can open trace files with the [Perfetto UI](https://ui.perfetto.dev/) to anaylze them and pinpoint potential optimizations. Perfetto features a timeline view that provides a visual representation of the trace.
You can use the W,A,S,D keys on your keyboard to zoom and pan, and your mouse to expand process tracks (rows) into their constituent thread tracks.
![perfetto-visualize](https://image.roku.com/ZHZscHItMTc2/perfetto-visualize.png)
## Adding custom trace data
You can use the roPerfetto BrightScript component to capture custom events in a Perfetto trace. The types of events you can record include instantaneous, duration, scoped, and flow events.
| **Event**  | **Description**  | **Example**  | **Snippet**  |
| --- | --- | --- | --- |
| Instantaneous  | Events without a duration  | keypress  |
```
tracer = CreateObject("roPerfetto")
tracer.instantEvent("my_instant_event")
tracer.instantEvent("my_instant_event", {debug_1: 42, debug_2: "hello"})

```
 |
| Duration  | Events with a beginning and an end  | long function  |
```
sub myfunc()
    tracer = CreateObject("roPerfetto")
    params = {debug_1: 42, debug_2: "hello"}
    tracer.beginEvent("my_duration_event", params)
    do_stuff()
    tracer.endEvent()
end sub

```
 |
| Scoped  | Similar to duration events, but the end-event is generated automatically when the object returned from the call is released.  |   |
```
sub myfunc()
    tracer = CreateObject("roPerfetto")
    params = {debug_1: 42, debug_2: "hello"}
    scoped_event = tracer.createScopedEvent("my_scoped_event", params)
    do_stuff()
    ' end event auto-created when scoped_event is released.
end sub

```
 |
| Flow  | Creation of a “flow” of events from one piece of code to another.  | A Task thread to the Render thread.  |
```
sub func1()
    flowId = 42   ' A user-selected unique unsigned integer identifier
    tracer = CreateObject("roPerfetto")
    tracer.flowEvent(flowId, "my_flow_event_1")
end sub
sub func2()
    flowId = 42
    tracer = CreateObject("roPerfetto")
    tracer.flowEvent(flowId, "my_flow_event_2")
end sub
sub func3()
    flowId = 42
    tracer = CreateObject("roPerfetto")
    tracer.terminateFlow(flowId, "my_flow_event_3")
end sub

```
 |
## Using PerfettoSQL to query traces
You can query the data in a trace using [PerfettoSQL](https://perfetto.dev/docs/analysis/perfetto-sql-getting-started) following these steps:
  1. Click **Query (SQL)** in the left sidebar in the Perfetto UI.
  2. Enter your query in the editor.
  3. Click **Run Query**.![perfetto-sql](https://image.roku.com/ZHZscHItMTc2/perfetto-sql.png)

The following examples demonstrate some of the use cases for querying your trace data:
| **Use case**  | **Query**  |
| --- | --- |
| Find all rendezvous in order of duration (long rendezvous often cause dropped frames and may indicate inefficient observer functions).  | `SELECT * FROM slices WHERE name = 'rendezvous' ORDER BY dur DESC;`  |
| Find long executions of swapBuffers which indicate places where the channel may be dropping frames  | `SELECT * FROM slice WHERE name = 'swapBuffers' ORDER BY dur DESC;`  |
| Find places where the channel is handling a key press with `OnKeyEvent()`  | `SELECT * FROM slice WHERE name = 'keyEvent' ORDER BY dur DESC;`  |
| Find all of the observers being called in the app.  | `SELECT * FROM slice WHERE name = 'observer.callback' ORDER BY dur DESC;`  |
| Find all of the places where the channel is calling `setField`.  | `SELECT * FROM slice WHERE name = 'roSGNode.setField' ORDER BY dur DESC;`  |
## Glossary
Roku's Perfetto-based app tracing solution exposes a number of terms that Roku developers may be unfamiliar with:
| Term  | Defintion  |
| --- | --- |
| SdkLauncher  | A Roku OS plugin that provides an environment for running SDK apps in a sandboxed process.  |
| PR_ui  | The main BrightScript thread.  |
| RenderThread  | The primary SceneGraph render thread.  |
| AuxRenderThread  | A Roku OS thread used to offload some rendering tasks from the main UI thread. This helps improve the responsiveness and smoothness of the user interface.  |
| TN:[function name]  | A Task thread spawned by a [**Task** node](https://developer.roku.com/docs/references/scenegraph/control-nodes/task.md) . The function name represents the name of the Task function defined by the app.  |
| ExecBrightScript  | A slice representing the BrightScript engine processing app code.  |
| render  | A slice representing the process of drawing or composing a frame for display.  |
| swapBuffers  | A slice representing the operation of presenting a newly rendered frame to the display.  |
| consumeAllTasks  | A slice representing the render thread as it is processing messages from the Render Thread Queue that are waiting. These can include rendezvous as well as messages sent using the [**roRenderThreadQueue** component](https://developer.roku.com/docs/references/brightscript/components/rorenderthreadqueue.md).  |
| bscCopyToDomainEx  | A slice representing data being copied. For example, when getting or setting a field on a [**Task** node](https://developer.roku.com/docs/references/scenegraph/control-nodes/task.md) from the Render thread.  |
## Video tutorial
This following video demonstrates how you can use Perfetto to record, analyze, and visualize traces of your Roku apps to pinpoint where you can reduce resource consumption and optimize performance.